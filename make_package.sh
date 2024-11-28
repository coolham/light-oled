#!/bin/bash

# 使用 PyInstaller 打包 Python 程序
APP_NAME="light-oled"
pyinstaller --noconfirm --name $APP_NAME main.py

# 创建目标目录
mkdir -p dist/$APP_NAM/conf
mkdir -p dist/$APP_NAM/fonts

# 复制 conf 目录
cp -r conf/* dist/$APP_NAM/conf/

# 复制 help 目录
cp -r fonts/* dist/$APP_NAM/fonts/

