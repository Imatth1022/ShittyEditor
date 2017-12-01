#!/usr/bin/python3

### A simple text editor ###
### Started on 11-29-17  ###
### Finished on          ###

from tkinter import *
from tkinter import ttk

# Builds generic window using Tkinter
root = Tk()
root.title(' A Shitty Editor. ')
frame = Frame(root)

# Display file name (label)
fileName = StringVar()
label = Label(frame, textvariable=fileName)
fileName.set('Untitled')

# Buttons
openbutton = Button(frame, text='Open')
saasbutton = Button(frame, text='Save as')
savebutton = Button(frame, text='Save')
# Text input
text = Text(frame)


# grid
frame.grid()
label.grid(row=0)
openbutton.grid(row=1, column=0)
saasbutton.grid(row=1, column=2)
savebutton.grid(row=1, column=1)


root.mainloop()
