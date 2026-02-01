[app]
title = Marketnite
package.name = marketnite
package.domain = org.marketnite
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Icon configuration
icon.filename = assets/logo.png

requirements = python3,kivy,kivymd,android,requests

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1