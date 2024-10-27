@echo off


cd /d C:\Users\mark\Documents\Github\RaysolApp\

::cd /d E:\TestMap\

:: Set the path to your virtual environment
set VENV_PATH=.\myenv

:: Check if the virtual environment already exists
if not exist "%VENV_PATH%\Scripts\activate" (
    echo Creating virtual environment...
    
    :: Create the virtual environment
    python -m venv %VENV_PATH%
    
    :: Create a .gitignore file
    echo /myenv/ > %VENV_PATH%\.gitignore
) else (
    echo Virtual environment already exists.
)

:: Activate the virtual environment
call %VENV_PATH%\Scripts\activate

:: Change the working directory
cd /d C:\Users\mark\Documents\Github\RaysolApp\
:: cd /d E:\Git\RaysolApp\
:: cd /d E:\TestMap\


:: Activate the virtual environment
 call myenv\Scripts\activate

pip install kaleido 

:: Update packages to their latest versions
 pip install -r requirements.txt --upgrade

:: Navigate to the SRC directory
cd SRC

:: Run the Python script
python app.py

:: Timeout for 3 seconds
timeout /t 3 /nobreak >nul

:: Open website
start http://127.0.0.1:8050/

:: Pause to keep the terminal open (optional)
pause