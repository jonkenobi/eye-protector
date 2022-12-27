import time
from tkinter import *

'''
An alarm to tell you to take a break after every BREAK_INTERVAL minutes
A popup window shows at the forefront of your windows every time.   

How to run 
To run, just run alarm.py in your command line 
'''
BREAK_INTERVAL = 20  # Minutes


def create_tk():
    win = Tk()

    # Set the size of the Tkinter frame
    height = win.winfo_screenheight()
    width = win.winfo_screenwidth()
    win.geometry("{0}x{1}+0+0".format(width, height))

    win.attributes('-topmost', True)  # Put tkinter as frontmost window on the screen
    # win.overrideredirect(True) # makes it full screen
    win.title("Take a break!")

    return win


print("Starting alarm for every {} minutes".format(BREAK_INTERVAL))
while True:
    time.sleep(BREAK_INTERVAL * 60)
    print("Take a break!")

    # the tk instance will be opened by the mainloop() function, but destroyed when window closed
    create_tk().mainloop()
    # winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
