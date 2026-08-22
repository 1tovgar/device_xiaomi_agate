/*
 * Copyright (C) 2021-2022 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_variant.h>
#include <libinit_utils.h>

#include "vendor_init.h"

static const variant_info_t agate_info = {
    .hwc_value = "",
    .sku_value = "agate",

    .brand = "Xiaomi",
    .device = "agate",
    .mod_device = "agate_global",
    .marketname = "Xiaomi 11T",
    .model = "21081111RG",
    .build_fingerprint = "Xiaomi/agate_global/agate:12/SP1A.210812.016/V816.0.17.0.UKWMIXM:user/release-keys",
};

static const std::vector<variant_info_t> variants = {
    agate_info,
};

void vendor_load_properties() {
    search_variant(variants);
}
