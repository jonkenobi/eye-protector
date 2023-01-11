# eye-protector
A simple python script that shows a popup for every interval of time. 
You can use it to remind you to take a break on your laptop, for example. 

### Installation requirements
Only python is needed! 
No extra package installations are necessary

### How to run
To run, just run `alarm.py` in your command line.

Every BREAK_INTERVAL minutes, this popup will show to remind you to take a break

![img.png](https://raw.githubusercontent.com/jonkenobi/eye-protector/master/tk_popup_img.jpg)

### To run the script on start of your Windows PC
1. Press Win+R, and enter `shell:startup`. Or go to `C:\Users\{UserName}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
2. Inside the folder, add a bat file. You can name it anything, such as `alarm.bat` 
```
::Replace directory with direct path to your forex-tool file
@C:\Users\Jonathan\miniconda3\python.exe C:\Users\Jonathan\PycharmProjects\eye-protector\alarm.py %*
@pause
```

