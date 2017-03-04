#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniel
#
# Created:     28/02/2017
# Copyright:   (c) Daniel 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Tkinter import *
import os
import subprocess

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame,
                             text="QUIT", fg="red",
                             command=quit)
        self.button.pack(side=TOP)
        self.slogan = Button(frame,
                             text="Hello",
                             command=self.write_slogan)
        self.slogan.pack(side=TOP)
    def run_app(script):
        s = os.getcwd() + "\\" + script + ".py"
        p = subprocess.Popen(["python",s], shell=False)
        return p

root = Tk()
app = App(root)
root.mainloop()