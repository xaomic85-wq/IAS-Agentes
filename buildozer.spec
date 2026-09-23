[app]
title = IAS-Agentes
package.name = iasagentes
package.domain = org.gnu.ias
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.ant_options = -Dfile.encoding=UTF-8
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
