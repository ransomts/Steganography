from Tkinter import *
from ImageTk import *
from tkMessageBox import *
from tkFileDialog import *

def how_to_use_command():
    print("foo")
    
def about_command():
    showinfo("About", 'Author: Tim Ransom\nMarch 2016')

def quit_command(master):
    master.destroy()

def read_text():
    # clear out what's already in the text area
    text_area.delete('1.0', END)
    filename = tkFileDialog.askopenfilename()
    with open(filename, 'r') as plaintext_file:
        text_area.insert('1.0', plaintext_file.read())

def open_encode_image(left_image):
    filename = askopenfilename()
    new_encode_image= PhotoImage(Image.open(filename))
    left_image.configure(image = new_encode_image)
    left_image.image = new_encode_image

def open_decode_image(right_image):
    filename = askopenfilename()
    new_encode_image= PhotoImage(Image.open(filename))
    right_image.configure(image = new_encode_image)
    right_image.image = new_encode_image


