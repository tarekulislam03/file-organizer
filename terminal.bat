@echo off
:: Open Command Prompt inside this folder

cd /d "%~dp0"
start cmd /k "cd /d %~dp0 && echo You are now inside: %cd%"
