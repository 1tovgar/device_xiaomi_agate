#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/mediatek',
    'hardware/xiaomi',
    'hardware/mediatek/libmtkperf_client',
    'device/xiaomi/agate',
    'vendor/xiaomi/agate'
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libimsma.so': blob_fixup()
        .add_needed('libshim_sink.so'),
    
    'vendor/lib/hw/audio.primary.mt6893.so': blob_fixup()
        .replace_needed('libalsautils.so', 'libalsautilsv2.so')
        .add_needed('libstagefright_foundation-v33.so'),

    ('vendor/bin/hw/android.hardware.media.c2@1.2-mediatek',
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b'): blob_fixup()
        .add_needed('libcodec2_hidl@1.0.so')
        .add_needed('libbase_shim.so')
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),
    
    ('vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so', 'vendor/lib64/libmtkcam_stdutils.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    
    ('vendor/lib64/libSQLiteModule_VER_ALL.so', 'vendor/lib64/lib3a.flash.so', 'vendor/lib64/lib3a.ae.stat.so', 'vendor/lib64/lib3a.sensors.color.so', 'vendor/lib64/lib3a.sensors.flicker.so', 'vendor/lib64/libaaa_ltm.so'): blob_fixup()
        .add_needed('liblog.so'),
    
    'vendor/bin/hw/camerahalserver': blob_fixup()
        .binary_regex_replace(b'/system/lib64', b'/vendor/lib64'),
    
    'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so': blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so','android.hardware.gnss-V1-ndk.so'),
    
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),

    'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service': blob_fixup()
        .replace_needed('android.hardware.power-V2-ndk_platform.so', 'android.hardware.power-V2-ndk.so')
        .remove_needed('android.hardware.power-service-mediatek.so'),
    
    ('vendor/lib/hw/vendor.mediatek.hardware.bluetooth.audio@2.2-impl.so', 'vendor/lib64/hw/vendor.mediatek.hardware.bluetooth.audio@2.2-impl.so'): blob_fixup()
        .replace_needed('vendor.mediatek.hardware.audio@6.1.so', 'vendor.mediatek.hardware.audio@7.1.so'),

    ('vendor/bin/hw/android.hardware.neuralnetworks@1.3-service-mtk-neuron', 'vendor/lib/libnvram.so', 'vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so'): blob_fixup()
        .add_needed('libbase_shim.so'),

    ('vendor/lib64/libalLDC.so', 'vendor/lib64/libalAILDC.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),

    'vendor/lib64/hw/hwcomposer.mt6893.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so')
        .binary_regex_replace(
            b'OnScreenFingerprintPressedIcon',
            b'SurfaceView[UdfpsControllerOve'
    ),

    'vendor/bin/mnld': blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'libsensorndkbridge-v30.so'),

    ('vendor/lib64/libaalservice.so', 'vendor/lib/libaalservice.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),

    'vendor/lib64/mt6893/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),

    'system_ext/lib64/libsource.so': blob_fixup()
        .add_needed('libui_shim.so'),

    ('vendor/lib/libthha.so', 'vendor/lib/libvcodec_oal.so'): blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    
    ('vendor/lib/libteei_daemon_vfs.so', 'vendor/lib64/libteei_daemon_vfs.so'): blob_fixup()
        .add_needed('liblog.so'),


    ('vendor/lib64/libalLDC.so', 'vendor/lib64/libalAILDC.so', 'vendor/lib64/libalhLDC.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    
}  # fmt: skip

module = ExtractUtilsModule(
    'agate',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
