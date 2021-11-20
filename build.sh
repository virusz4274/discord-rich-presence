#!/bin/bash
pyinstaller --onefile app.py
cp main_ui.ui dist/main_ui.ui
mkdir finalpackage
tar -cvf finalpackage/linux.tar dist/*
