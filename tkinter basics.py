"""
This file contains the basic things in Tkinter and learning them, it basically exists so i can copy paste the things
For detailed more information, go to Jupyter -> learning tkinter.ipynp
"""

# importing the things
import tkinter as tk
import pytube as pt
import urllib.request
import os
import re


# Some constants
HEIGHT = 500
WIDTH = 600
# Starting the loop
root = tk.Tk()

# Creating the Canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

image1 = tk.PhotoImage(file="dopus.png")
image1label = tk.Label(canvas, image=image1)
image1label.place(relwidth=1, relheight=1)
# Creating the Frame
frame = tk.Frame(root, bg='#80c1ff')

frame.place(relwidth=1, relheight=1)  # this is going to fill the entire screen

# relwidth and relwidth is relative tot he width, and obviously, coz it's the child of root, it's going to be relative to root
frame.place(relwidth=0.5, relheight=0.5)  # this is going to fill half the root

# now if you want to offset this thing from teh screen somewhere, then you use the rely and the relx functions
# this is also relative as in you can just resize it.
frame.place(rely=0.1, relx=0.1, relwidth=0.8, relheight=0.8)  # this is going to fill half the root

# Creating the button
button = tk.Button(frame, text="Text button", bg='blue', fg='red')
button.place(rely=0, relx=0, relwidth=0.25, relheight=0.2)

# creatign the label
label = tk.Label(frame, bg='green', text='This is some')
# this is going to happen relative to the frame
label.place(rely=0, relx=0.26, relwidth=0.25, relheight=0.2)

entry = tk.Entry(frame, bg='red')
# also going to be relative to the frame thing
entry.place(rely=0, relx=0.52, relwidth=0.2, relheight=0.2)

root.mainloop()
