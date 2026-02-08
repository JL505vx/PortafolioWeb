@echo off
REM Arranca Django en el puerto 8013 (localhost)
cd /d "%~dp0"
python manage.py runserver 127.0.0.1:8013
