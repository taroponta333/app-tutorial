[app]
title = Offline Video Converter
package.name = offlineconverter
package.domain = com.example.ffmpeg

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
# ffmpeg バイナリをAPK内に同梱する指定
source.include_patterns = ffmpeg

version = 0.1

# 必要なライブラリ
requirements = python3,kivy

# 画面の向き（縦画面固定）
orientation = portrait

# ターゲットアーキテクチャ (arm64 のみにしてビルド時間を短縮)
android.archs = arm64-v8a

# Androidの権限
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# NDK/SDKの自動受諾
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
