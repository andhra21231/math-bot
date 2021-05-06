@echo off &  setlocal enabledelayedexpansion

title Mathematic Bot X MusicBot(Develop Mode) >nul 2>&1

goto presentation
:presentation


echo    V H C I D . T E C H O L O G Y
echo    =============================
echo               presents
echo    =============================

echo Welcome To : VHID.TECH Project

echo Author By : Zack_#4064
echo helping dev : CoolNuttle#3261               


goto checking_py

:checking_py
echo checking if python is installed
python --version
echo checking if pip is installed
pip --version
echo -----------------------------
echo BEWARE : YOU MUST HAVE PYTHON
echo       3.6 + AND PIP
echo -----------------------------



goto installer

:installer
echo No Need PIP Installer Now!
goto pilihan

:pilihan

ECHO Please turn on CAPS Lock
ECHO 1. Basic Math[1]
ECHO 2. Area Math [2]
ECHO 3. Volume Math [3]
ECHO 4. Perimeter Math [4]
ECHO 5. Hypotenus Math [5]
ECHO (Other Math / Music Coming Soon)
ECHO 6.Exit [E]
ECHO.
CHOICE /C 123456E /M "What Do You Want To Start ?"
IF ERRORLEVEL 6 exit
IF ERRORLEVEL 5 GOTO mulai_hypotenus
IF ERRORLEVEL 4 GOTO mulai_perimeter
IF ERRORLEVEL 3 GOTO mulai_volume
IF ERRORLEVEL 2 GOTO mulai_area
IF ERRORLEVEL 1 GOTO mulai_basic

:mulai_basic
python core_script/+_-_x.py


goto pilihan

:mulai_area
python core_script/areas.py


goto pilihan

:mulai_volume
python core_script/volume.py

goto pilihan

:mulai_perimeter
python core_script/perimeter.py

goto pilihan

:mulai_hypotenus
python core_script/hypotenus.py
