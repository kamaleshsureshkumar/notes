[app]

title = Notes
package.name = notes
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
# Keep the Python recipe unpinned: python-for-android manages the compatible
# hostpython3 version for the selected toolchain. Pinning python3==3.11.9 caused
# a hostpython3 mismatch (3.11.9 != 3.14.2) in CI.
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.sdk_path = /opt/Android/Sdk
android.build_tools_version = 33.0.2
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.python_version = 3

[buildozer]
log_level = 2
warn_on_root = 1
