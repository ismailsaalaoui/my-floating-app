# This .spec config file tells Buildozer an app's requirements for being built.

[app]

# (str) Title of your application
title = Floating Button App

# (str) Package name
package.name = floatingapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.floating.app

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (leave empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (leave empty to not exclude anything)
source.exclude_dirs = tests, bin, venv, .buildozer

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# Android specific settings
android.skip_update = True
android.api = 33
android.minapi = 24
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.ndk = 25b
android.ndk_api = 21

# (list) The Android archs to build for
android.archs = arm64-v8a,armeabi-v7a

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Supported orientations
orientation = portrait

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Permissions
android.permissions = android.permission.INTERNET

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (bool) indicates Android auto backup feature (Android API >=23)
android.allow_backup = True

# Python for android
p4a.bootstrap = sdl2
p4a.setup_py = false

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

ios.codesign.allowed = false

[buildozer]

log_level = 2
warn_on_root = 1
