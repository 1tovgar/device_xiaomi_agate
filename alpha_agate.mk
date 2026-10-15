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

# Inherit some common AlphaDroid stuff.
$(call inherit-product, vendor/alpha/config/common_full_phone.mk)

TARGET_HAS_UDFPS := false
TARGET_SUPPORTS_BLUR := 2
TARGET_FACE_UNLOCK_SUPPORTED := true

TARGET_INCLUDE_SIMPLE_TUNE := true
TARGET_SUPPORTS_QUICK_TAP := true
#TARGET_SUPPORTS_CALL_RECORDING := false # https://github.com/crdroidandroid/android_vendor_bcr.git
TARGET_INCLUDE_STOCK_ARCORE := true


# 1 for vanilla, 2 for gapps(discontinued ?), 3 for gms
TARGET_BUILD_PACKAGE := 3

# Debug
WITH_ADB_INSECURE := true

ALPHA_MAINTAINER := tovgar

PRODUCT_NAME := alpha_agate
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

# Boot animation
TARGET_SCREEN_HEIGHT := 2400
TARGET_SCREEN_WIDTH := 1080
TARGET_BOOT_ANIMATION_RES := 1080
