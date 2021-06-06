@echo off

echo ###################################
echo #           VHCID TECH            #
echo #         Production 2021         #
echo #                                 #
echo #        Under MIT Lisence        #
echo #      Development By : Zack_     #
echo ###################################

timeout /t 5 >nul
cls

echo 1. YES [Y]
echo 2. NO [N]
echo 3. GOTO LAUNCH [G]
CHOICE /C YNG /M "Are You Want To Download All Dependencies For Better Experience ?"
IF ERRORLEVEL 3 GOTO launcher
IF ERRORLEVEL 2 exit
IF ERRORLEVEL 1 GOTO depen

:depen
CLS
echo ##################################
echo #                                #
echo #      You Must Have This !      #
echo #         Python 3.6 ++          # 
echo #                                #
echo #       And PIP Installer        #
echo ##################################
timeout /t 5 >nul

cls
echo You Can Donate Me At https://paypal.me/rainver
echo Pls Donate :3

timeout /t 5 >nul

cls 
echo ok Lets Begin Download Dependencies
timeout /t 2 >nul
echo first Lets Checking If Python Is Installed At Your Computer !

python

python exit()
cls
pip -V
timeout /t 3 >nul
cls
echo Ok Thats Enough :)
echo Now Let Me Download ALL of Dependencies
timeout /t 1 >nul
cls
echo First, I Want To Download PyQt5
pip install PyQt5
cls
echo Its Is Done ? Ohh Its Done !
timeout /t 2 >nul
echo Now I Want To Download Cores, MATH PIP :/
timeout /t 2>nul 
cls
echo IYA [1]
echo TIDAK [2]
CHOICE /C 12 /M "Apakah Ingin Melanjutkan Ke Bot ?"
IF ERRORLEVEL 2 GOTO exit
IF ERRORLEVEL 1 GOTO launcher

:launcher
cls
echo #############################
echo #      VHC TECHONLOGY       #
echo #                           #
echo #       P R E S E N T       #
echo #      Version : 0.3.5      #
echo #############################
echo Loading Information Please Wait...
timeout /t 4>nul 
cls
cd ./core_script/__pycache__/dist/menu
start menu.exe

