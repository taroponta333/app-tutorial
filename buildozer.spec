[app]

# (str) Title of your application
title = 真UFC

# (str) Package name
package.name = trueufc

# (str) Package domain (needed for android packaging)
package.domain = org.converter

# (list) Source files to include (let it include py,png,etc)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it exclude conventionals)
source.exclude_exts = spec

# (list) List of directory to exclude from source dir
source.exclude_dirs = bin, venv, .git, .github

# (list) Application requirements
# python-for-android 用のパッケージ名（PILはpillow、ffmpegラッパーはffmpeg-python）
requirements = python3,kivy,pillow,ffmpeg-python,ffmpeg

# (str) Version of the application
version = 1.0

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services = 

#
# Options
#

# (str) Custom icon (path relative to buildozer.spec)
icon.filename = %(source.dir)s/icon.png

# (str) Custom pre-splash screen
#presplash.filename = %(source.dir)s/splash.png

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (list) Features
#android.features = 

# (int) Target Android API, should be as high as possible.
#android.api = 33

# (int) Minimum API your APK will support.
#android.minapi = 21

# (str) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 25b

# (str) Android entry point, default is ok for Kivy app
#android.entrypoint = org.renpy.android.PythonActivity

# (list) Application bounaries to whitelist
#android.whitelist = 

# (bool) Indicate whether the application should be full screen or not
android.fullscreen = False

# (string) Android app theme, default is ok for Kivy app
#android.theme = @android:style/Theme.NoTitleBar.Fullscreen

# (list) The Android archs to build for,, and of: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) If True, then skip trying to update the Android SDK
#android.skip_update = False

# (bool) If True, automatically accept SDK license agreements.
android.accept_sdk_license = True

# (str) OUGC keystore password
#android.keystore_password = 

# (str) OUGC key alias password
#android.keyalias_password = 


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact, relative to the spec
bin_dir = ./bin

# (str) Path to build directory (where the apps are built)
#build_dir = ./.buildozer

# (str) Path to Python for Android (p4a)
#p4a.source_dir =
