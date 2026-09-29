#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from device makefile.
$(call inherit-product, device/xiaomi/agate/device.mk)

# Inherit LineageOS product
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_agate
PRODUCT_DEVICE := agate
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := M2104K11TC

PRODUCT_CHARACTERISTICS := nosdcard

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildFingerprint=Redmi/agate/agate:12/SP1A.210812.016/V14.0.6.0.TKWMIXM:user/release-keys \
    DeviceProduct=agate \
    SystemName=agate
