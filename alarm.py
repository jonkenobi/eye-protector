import time
from tkinter import *

'''
An alarm to tell you to take a break after every BREAK_INTERVAL minutes
A popup window shows at the top of your windows every time.   

How to run 
To run, just run alarm.py in your command line 
'''
BREAK_INTERVAL = 20  # Minutes

def create_tk():
    win = Tk()
    # Set the geometry of Tkinter frame
    win.geometry("1000x500")
    win.attributes('-topmost', 1)
    win.attributes('-topmost', 0)
    win.title("Take a break!")
    return win


print("Starting alarm")
while True:
    time.sleep(BREAK_INTERVAL*60)
    print("Take a break!")

    # the tk instance will be opened by the mainloop() function, but destroyed when window closed
    create_tk().mainloop()
    # winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
