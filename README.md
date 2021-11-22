# discord-rich-presence
A Discord Rich Presence App to set your own custom rich presence.

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

## HOW TO USE
* RUN THE PROGRAM
* PRESS THE LOAD BUTTON TO LOAD DEFAULT PROFILE
* MAKE CHANGES TO PROFILE AND CLICK ON SAVE
* CLICK ON NEW TO CREATE MULTIPLE PROFILES
* AFTER CLICKING NEW LOAD THE NEW PROFILE THEN START MAKING CHANGES
* THE APP WILL CLOSE IF DISCORD IS NOT OPEN
* APP WILL CLOSE ABRUTLY IF THE INSTRUCTION TO CREATE NEW PROFILE IS NOT LOADED
* TO STOP THE APP, YOU CANT!. YOU NEED TO FORCE CLOSE INORDER TO STOP THE APP (WILL BE FIXED)

## REPORT ISSUES

Either create an issue in discord or message me in telegram t.me/virusz4274
Please provide how it crashed so that i can try to recreate the problem that you faced.


## BUILDS
Ready to use package are available inside "finalpackage" folder, no need to install any depedency just run the app. There is a slight chance Antivirus might call it a virus / trojan, it is a false alarm. If you are not confident or dont trust you can build the package following the instructions below.

[Linux](https://github.com/virusz4274/discord-rich-presence/releases)

[Windows](https://github.com/virusz4274/discord-rich-presence/releases)



## Depedency
* Python
* pip
* pipenv ( if you have pip , ```run pip install pipenv``` )

## To Run#
* ```pipenv shell```
* ```python app.py```

## To Build Package
* ```pipenv shell```
* ```pipenv install --dev```
*  For Linux 
    * ```./build.sh```
    * You will get a tar package inside "finalpackage" folder
*  For Windows 
    * ```pyinstaller --noconsole --onefile app.py```
    * copy main_ui.ui to "dist" folder , you can compress  the dist folder and send it or use the application by opening "app"
