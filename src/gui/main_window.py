#!/usr/bin/python

from Tkinter import *
from ImageTk import *
from tkMessageBox import *
from button_commands import *


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
left_image.bind("<Button-1>", lambda e: open_encode_image(left_image))

right_image = Label(master, text="Second", image=decode_image)
right_image.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)
right_image.bind("<Button-1>", lambda e: open_decode_image(right_image))

text_area = Text(master, height=10, width=50)
text_area.grid(row=2, column=0, rowspan=3, sticky=W+E+N+S)

encode_lableframe = LabelFrame(master, text='Encode Input')
encode_lableframe.grid(row = 2, column = 1, columnspan=2, sticky=W+E+N+S)

encode_variable = StringVar()
encode_variable.set("Text Area")

encode_rb_1 = Radiobutton(encode_lableframe, text='Text Area',
                          variable=encode_variable, value="Text Area")
encode_rb_1.grid(row=0,column=0, sticky=W)

encode_rb_2 = Radiobutton(encode_lableframe, text='File',
                          variable=encode_variable, value="File")
encode_rb_2.grid(row=1,column=0, sticky=W)

encode_variable = StringVar()
encode_variable.set("Text Area")
decode_lableframe = LabelFrame(master, text='Decode Input')
decode_lableframe.grid(row = 3, column = 1, columnspan=2, sticky=W+E+N+S)

decode_rb_1 = Radiobutton(decode_lableframe, text='Text Area',
                          variable=encode_variable, value="Text Area")
decode_rb_1.grid(row=0,column=0, sticky=W)

decode_rb_2 = Radiobutton(decode_lableframe, text='File',
                          variable=encode_variable, value="File")
decode_rb_2.grid(row=1,column=0, sticky=W)

decode_button = Button(master, text='Encode')
decode_button.grid(row=4, column=1, sticky=W+E)

decode_button = Button(master, text='Decode')
decode_button.grid(row=4, column=2, sticky=W+E)

        
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='Read text from file', command=read_text)
filemenu.add_command(label='Open image to encode', command=lambda e: open_encode_image())
filemenu.add_command(label='Open image to decode', command=lambda e: open_decode_image())


helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label='How to use', command=how_to_use_command)
helpmenu.add_command(label='About', command=about_command)
helpmenu.add_command(label='Quit', command=lambda e:quit_command(), underline=0, accelerator="C-q")


menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Help', menu=helpmenu)

master.bind("<Control-q>", lambda e: quit_command(master))
master.config(menu=menubar)

mainloop()
