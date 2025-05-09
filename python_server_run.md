### For Python Server run
open note pad and write syntext and save runserver.bat

```
@echo off

REM Activate virtual environment
call D:\Dev\env\Scripts\activate.bat

REM Navigate to the Django project directory
cd /d D:\Dev\prosaanti

REM Start the Django development server
python manage.py runserver

pause
```
