#!/usr/bin/python

from Tkinter import *
from ImageTk import *
from tkMessageBox import *
import tkFileDialog
from Button_Commands import *

master = Tk()
master.columnconfigure(0, weight=2)
master.columnconfigure(1, weight=1)
master.columnconfigure(2, weight=1)
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)

encode_image = PhotoImage(file="../../images/cat.png")
decode_image = PhotoImage(Image.open("../../images/cat.png"))

left_image = Label(master, text="First", image=encode_image)
left_image.grid(row=0, column=0, sticky=W+E+N+S)

right_image = Label(master, text="Second", image=decode_image)
right_image.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)

text_area = Text(master, height=10, width=50)
text_area.grid(row=2, column=0, rowspan=3, sticky=W+E+N+S)

encode_lableframe = LabelFrame(master, text='Encode Input')
encode_lableframe.grid(row = 2, column = 1, columnspan=2, sticky=W+E+N+S)

#encode_rb_1 = RadioButton(master, text = 'text area')
#encode_rb_1.grid(row=0,column=0)
#encode_rb_2 = RadioButton(encode_lableframe, text = 'file')

decode_lableframe = LabelFrame(master, text='Decode Input')
decode_lableframe.grid(row = 3, column = 1, columnspan=2, sticky=W+E+N+S)

encode_button = Button(master, text='Encode')
encode_button.grid(row=4, column=1, sticky=W+E)

decode_button = Button(master, text='Decode')
decode_button.grid(row=4, column=2, sticky=W+E)



#display_text_button = Button(master, text='Display Text', command=display_text)
#display_text_button.grid(row=4, column=1)

        
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='Read text from file', command=read_text)
filemenu.add_command(label='Open image to encode', command=open_encode_image)
filemenu.add_command(label='Open image to decode', command=open_decode_image)

def quit_command():
    master.destroy()

helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label='How to use', command=how_to_use_command)
helpmenu.add_command(label='About', command=about_command)
helpmenu.add_command(label='Quit', command=quit_command, underline=0, accelerator="C-q")


menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Help', menu=helpmenu)

master.bind("<Control-q>", quit_command)
master.config(menu=menubar)

mainloop()
