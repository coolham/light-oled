#!/bin/bash

# 使用 PyInstaller 打包 Python 程序
pyinstaller --noconfirm --name light-oled main.py

# 创建目标目录
mkdir -p dist/light-oled/conf
mkdir -p dist/light-oled/fonts

# 复制 conf 目录
cp -r conf/* dist/light-oled/conf/

# 复制 help 目录
cp -r fonts/* dist/light-oled/fonts/

