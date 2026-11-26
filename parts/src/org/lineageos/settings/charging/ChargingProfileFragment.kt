/*
 * SPDX-FileCopyrightText: 2026 The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

package org.lineageos.settings.charging

import android.os.Bundle
import androidx.preference.ListPreference
import androidx.preference.PreferenceFragment
import org.lineageos.settings.R

/** Charging power profile settings. */
class ChargingProfileFragment : PreferenceFragment() {

    override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
        addPreferencesFromResource(R.xml.charging_settings)

        ChargingProfileUtils.init(activity ?: return)
        findPreference<ListPreference>(KEY_PROFILE)?.apply {
            value = ChargingProfileUtils.profile.toString()
            setOnPreferenceChangeListener { _, newValue ->
                ChargingProfileUtils.selectProfile((newValue as String).toIntOrNull() ?: 0)
                true
            }
        }
    }

    companion object {
        private const val KEY_PROFILE = "charging_profile"
    }
}
