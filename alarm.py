import time
import tkinter as tk
from tkinter import *

'''
An alarm to tell you to take a break after every BREAK_INTERVAL minutes
A popup window shows at the forefront of your windows every time.
The popup counts down BREAK_LENGTH seconds during the break time   

How to run 
Just run alarm.py in your command line 
'''
BREAK_INTERVAL = 20  # Minutes
BREAK_LENGTH = 20  # Seconds


def create_tk():
    win = Tk()

    # Set the size of the Tkinter frame
    height = win.winfo_screenheight()
    width = win.winfo_screenwidth()
    win.geometry("{0}x{1}+0+0".format(width, height))

    win.attributes('-topmost', True)  # Put tkinter as frontmost window on the screen
    # win.overrideredirect(True) # makes it full screen

    win.title("Take a break!")
    seconds_unit_text = Label(win, text="secs", font=("Arial", 40, ""))
    seconds_unit_text.place(x=width / 2, y=height / 2 - 55)

    return win


def countdown(count):
    # change text in label
    seconds_label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count - 1)


print("Starting alarm for every {} minutes".format(BREAK_INTERVAL))

while True:
    time.sleep(BREAK_INTERVAL * 60)
    print("Take a break!")

    # the tk instance will be opened by the mainloop() function, but destroyed when window closed
    root = create_tk()

    # Create seconds countdown text
    seconds_label = tk.Label(root, font=("Times New Roman", 80, ""))

    # Place seconds countdown text todo refactor
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    seconds_label.place(x=width / 2 - 120, y=height / 2 - 100)

    countdown(BREAK_LENGTH)

    root.mainloop()
    t = time.localtime()
    current_time = time.strftime("%H: %M: %S", t)
    print("Took a break at " + current_time)
    # winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
