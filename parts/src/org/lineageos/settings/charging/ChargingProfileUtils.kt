/*
 * SPDX-FileCopyrightText: 2026 The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

package org.lineageos.settings.charging

import android.content.Context
import android.util.Log
import org.lineageos.settings.utils.writeLine

/**
 * Caps charging power by limiting the input current of both LN8000 charge
 * pumps (µA, per pump) and the PD adapter's max wattage.
 *
 * These are upper limits: the adapter/cable still decides the final wattage.
 */
object ChargingProfileUtils {
    private const val TAG = "ChargingProfile"

    private const val PREFS_NAME = "charging_profile"
    private const val KEY_PROFILE = "profile"

    private const val MASTER_ICL =
        "/sys/class/power_supply/bq2597x-master/input_current_limit"
    private const val SLAVE_ICL =
        "/sys/class/power_supply/bq2597x-slave/input_current_limit"
    private const val PDC_MAX_WATT = "/sys/devices/platform/mt_charger/pdc_max_watt"

    /** profile -> (input current limit in µA per pump, PD max watt) */
    private val PROFILES =
        mapOf(
            0 to (3050000 to 67), // stock dual-pump limit, ~67 W
            1 to (1500000 to 33), // ~33 W
            2 to (1000000 to 18), // ~18 W
        )

    private fun prefs(context: Context) =
        context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)

    var profile: Int
        get() = prefsHolder?.getInt(KEY_PROFILE, 0) ?: 0
        private set(value) {
            prefsHolder?.edit()?.putInt(KEY_PROFILE, value)?.apply()
            apply(value)
        }

    private var prefsHolder: android.content.SharedPreferences? = null

    fun init(context: Context) {
        prefsHolder = prefs(context)
    }

    fun selectProfile(profile: Int) {
        this.profile = PROFILES.containsKey(profile).let { if (it) profile else 0 }
    }

    fun onBootCompleted(context: Context) {
        init(context)
        apply(profile)
    }

    private fun apply(profile: Int) {
        val (icl, watt) = PROFILES[profile] ?: PROFILES[0]!!
        val masterOk = writeLine(MASTER_ICL, icl.toString())
        val slaveOk = writeLine(SLAVE_ICL, icl.toString())
        val pdOk = writeLine(PDC_MAX_WATT, watt.toString())
        Log.i(
            TAG,
            "Applied profile $profile (icl=$icl, pd=$watt): master=$masterOk slave=$slaveOk pd=$pdOk"
        )
    }
}
