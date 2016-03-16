from Tkinter import *
from ImageTk import *
from tkMessageBox import *
from tkFileDialog import *
from encrypt import *
from decrypt import *

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

def open_encode_image(left_image, new_image_filename=None):
    filename = askopenfilename() if new_image_filename == None else new_image_filename
    new_encode_image= PhotoImage(Image.open(filename))
    left_image.configure(image = new_encode_image)
    left_image.image = new_encode_image

def open_decode_image(right_image, new_image_filename=None):
    filename = askopenfilename() if new_image_filename == None else new_image_filename
    new_encode_image= PhotoImage(Image.open(filename))
    right_image.configure(image = new_encode_image)
    right_image.image = new_encode_image

def encode_button_command(encode_image, decode_image, text_area):
    new_image_filename = encode_text(text_area.get("1.0", END), encode_image)
    open_decode_image(decode_image, new_image_filename)
    showinfo("Encode", "Encoding Complete")

def decode_button_command(decode_image_filename, text_area):
    message=decode_text(decode_image_filename)
    text_area.delete("1.0", END)
    text_area.insert(END, message)
    showinfo("Decode", "Decoding Complete")
