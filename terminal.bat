@echo off
set PYTHON_DIR=%~dp0\python-3.12-embed
set PATH=%PYTHON_DIR%;%PATH%
cd /d "%~dp0"
%PYTHON_DIR%\python.exe main.py
pause
