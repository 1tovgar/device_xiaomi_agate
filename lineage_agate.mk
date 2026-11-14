#
# Copyright (C) 2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from device makefile.
$(call inherit-product, device/xiaomi/agate/device.mk)

# Inherit some common LineageOS stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_agate
PRODUCT_DEVICE := agate
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := 21081111RG
PRODUCT_SYSTEM_NAME := amber

PRODUCT_CHARACTERISTICS := nosdcard
PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildFingerprint=Xiaomi/amber_global/amber:12/SP1A.210812.016/V816.0.17.0.UKWMIXM:user/release-keys \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)


#RisingOS-specific
RISING_MAINTAINER="tovgar" #lunch

PRODUCT_BUILD_PROP_OVERRIDES += \
    RisingChipset="Mediatek Dimensity 1200" \
    RisingMaintainer="tovgar"

RISING_MAINTAINER := tovgar

TARGET_ENABLE_BLUR := true

PRODUCT_NO_CAMERA := false

# CORE build flags
WITH_GMS := true
TARGET_USES_PICO_GAPPS := true

# VANILLA only build flags
#WITH_GMS := false

# VANILLA build with MICROG
#WITH_GMS := false
#WITH_MICROG := true

# Boot animation
TARGET_SCREEN_HEIGHT := 2400
TARGET_SCREEN_WIDTH := 1080
TARGET_BOOT_ANIMATION_RES := 1080
