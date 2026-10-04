#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/agate

# OTA assert
TARGET_OTA_ASSERT_DEVICE := agate,agatein,amber

# Display
TARGET_SCREEN_DENSITY := 440

# Properties
TARGET_SYSTEM_PROP += $(DEVICE_PATH)/system.prop
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop

# Security Patch Level
VENDOR_SECURITY_PATCH := 2023-10-01

# Inherit from mt6893-common
include device/xiaomi/mt6893-common/BoardConfigCommon.mk

# Kernel / DTB
BOARD_PREBUILT_DTBIMAGE_DIR := $(DEVICE_PATH)-kernel/dtb
BOARD_VENDOR_KERNEL_MODULES := $(wildcard $(DEVICE_PATH)-kernel/modules/*.ko)

# Recovery
TARGET_RECOVERY_PIXEL_FORMAT := BGRA_8888

BOARD_PRODUCTIMAGE_MINIMAL_PARTITION_RESERVED_SIZE := false
-include vendor/halcyon/config/BoardConfigReservedSize.mk

# Inherit the proprietary files
-include device/xiaomi/miuicamera-agate/BoardConfig.mk
include vendor/xiaomi/agate/BoardConfigVendor.mk
