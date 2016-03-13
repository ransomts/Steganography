#!/usr/bin/python

from Tkinter import *
from ImageTk import *
import tkMessageBox, tkFileDialog

master = Tk()
master.columnconfigure(0, weight=2)
master.columnconfigure(1, weight=1)
master.columnconfigure(2, weight=1)
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)

encode_image = PhotoImage(file="../../images/cat.png")
decode_image = PhotoImage(Image.open("../../images/cat.png"))

left_image = Label(master, text="First", image=encode_image)
left_image.grid(row=0, column=0)

right_image = Label(master, text="Second", image=decode_image)
right_image.grid(row=0, column=1)

text_area = Text(master, height=10, width=50)
text_area.grid(row=2, column=0, rowspan=2, sticky=W+E+N+S)

encode_lableframe = LabelFrame(master, text='Encode Input')
encode_lableframe.grid(row = 2, column = 1)

#encode_rb_1 = RadioButton(master, text = 'text area')
#encode_rb_1.grid(row=0, column=0)
#encode_rb_2 = RadioButton(encode_lableframe, text = 'file')

encode_button = Button(master, text='Encode')
encode_button.grid(row=4, column=1, sticky=W+E)

decode_button = Button(master, text='Decode')
decode_button.grid(row=4, column=2, sticky=W+E)

def display_text():
    tkMessageBox.showinfo("Text in bar", text_area.get("1.0", END))


#display_text_button = Button(master, text='Display Text', command=display_text)
#display_text_button.grid(row=4, column=1)

def read_text():
    # clear out what's already in the text area
    text_area.delete('1.0', END)
    filename = tkFileDialog.askopenfilename()
    with open(filename, 'r') as plaintext_file:
        text_area.insert('1.0', plaintext_file.read())


def open_encode_image():
    filename = tkFileDialog.askopenfilename()
    new_encode_image= PhotoImage(Image.open(filename))
    left_image.configure(image = new_encode_image)
    left_image.image = new_encode_image

def open_decode_image():
    filename = tkFileDialog.askopenfilename()
    new_encode_image= PhotoImage(Image.open(filename))
    right_image.configure(image = new_encode_image)
    right_image.image = new_encode_image
        
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Read Text From File', command=read_text)
filemenu.add_command(label='Open image to encode', command=open_encode_image)
filemenu.add_command(label='Open image to decode', command=open_decode_image)

menubar.add_cascade(label='File', menu=filemenu)

master.config(menu=menubar)

mainloop()
