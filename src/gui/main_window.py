#!/usr/bin/python

from Tkinter import *
from ImageTk import *
import tkMessageBox, tkFileDialog

master = Tk()
master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)

encode_image = PhotoImage(Image.open("../../images/cat.png"))
decode_image = PhotoImage(Image.open("../../images/cat.png"))

#left_image = Label(master, text="First", image=encode_image).grid(row=0, column=0)
left_image = Canvas(master, width=300, height=300).grid(row=0, column=0)
left_image.create_image(0,0,image=encode_image)
print("one: " + str(type(left_image)))

right_image = Label(master, text="Second", image=decode_image).grid(row=0, column=1)

info_label = Label(master, text="info")
info_label.grid(row=1, columnspan=2)

text_area = Text(master, height=10, width=50)
text_area.grid(row=2, column=0, rowspan=2)

# make button
select_plaintext_file_button = Button(master, text='Select File')
#place it in the grid
select_plaintext_file_button.grid(row=2, column=1)

encode_decode_button = Button(master, text='Encode').grid(row=3, column=1)

def display_text():
    tkMessageBox.showinfo("Text in bar", text_area.get("1.0", END))


display_text_button = Button(master, text='Display Text', command=display_text)
display_text_button.grid(row=4, column=1)

def read_text():
    # clear out what's already in the text area
    text_area.delete('1.0', END)
    filename = tkFileDialog.askopenfilename()
    with open(filename, 'r') as plaintext_file:
        text_area.insert('1.0', plaintext_file.read())

def open_encode_image():
    print("two: " + str(type(left_image)))
    filename = tkFileDialog.askopenfilename()
    #new_encode_image = PhotoImage(Image.open(filename))
    #update the label image
    #left_image.configure(image=new_encode_image)
    img2 = PhotoImage(Image.open(filename))
    left_image.configure(image = img2)
    left_image.image = img2
        
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Read Text From File', command=read_text)
filemenu.add_command(label='Open image to encode', command=open_encode_image)
menubar.add_cascade(label='File', menu=filemenu)
master.config(menu=menubar)
mainloop()
