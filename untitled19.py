#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:42:17 2022

@author: riddhiekajain
"""

from tkinter import *
import random
root=Tk()
root.title("dictionary")
root.geometry("600x600")
dictionary={"Colours": ["marron1", "lawn green", "magenta2", "purple1", "springgreen2", "chocolate1","deeppink", "cyan" ]}

def bg1(): 
    randomno=random.randint(0, 7)
    print(dictionary["Colours"][randomno])
    root.configure(background=dictionary["Colours"][randomno])
    
button=Button(root, text="click me", command=bg1)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()