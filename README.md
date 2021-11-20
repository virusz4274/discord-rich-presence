# discord-rich-presence
A Discord Rich Presence App to set your own custom rich presence.

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)


##Depedency
* Python
* pip
* pipenv ( if you have pip , ```run pip install pipenv``` )

##To Run
* ```pipenv shell```
* ```python app.py```

##To Build Package
* ```pipenv shell```
* ```pipenv install --dev```
*  For Linux 
    * ```./build.sh```
    * You will get a tar package inside "finalpackage" folder
*  For Windows 
    * ```pyinstaller --onefile app.py```
    * copy main_ui.ui to "dist" folder , you can compress  the dist folder and send it or use the application by opening "app"
