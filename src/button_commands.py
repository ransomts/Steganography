from Tkinter import *
from ImageTk import *
from tkMessageBox import *
from tkFileDialog import *
from encrypt import *
from decrypt import *

def how_to_use_command():
    showinfo('How to use', "<fill in later>")
    
def about_command():
    showinfo('About', 'Author: Tim Ransom\nMarch 2016')

def quit_command(master):
    master.destroy()

def read_text(text_area, encode_variable):
    # clear out what's already in the text area
    text_area.delete('1.0', END)
    filename = askopenfilename()
    if filename != () and filename != '':
        with open(filename, 'r') as plaintext_file:
            text_area.insert('1.0', plaintext_file.read())
    encode_variable.set('Text Area')

def open_encode_image(left_image, right_image, left_image_filename):
    filename = askopenfilename()
    if filename != () and filename != '':
        left_image_filename.set(filename)
        new_encode_image= PhotoImage(Image.open(filename))
        left_image.configure(image = new_encode_image)
        left_image.image = new_encode_image

        right_image.configure(text='The encoded image will be displayed here after encode is hit',image='')

def open_decode_image(right_image, left_image, right_image_filename):
    filename = askopenfilename()
    if filename != () and filename != '':
        right_image_filename.set(filename)
        new_encode_image= PhotoImage(Image.open(filename))
        right_image.configure(image = new_encode_image)
        right_image.image = new_encode_image

        left_image.configure(image='', text='Image output will be displayed in the text area')

def push_decode_image(filename):
    new_encode_image= PhotoImage(Image.open(filename))
    right_image.configure(image = new_encode_image)
    right_image.image = new_encode_image
            
def encode_button_command(encode_image, decode_image, text_area, encode_image_filename):
    push_decode_image(encode_text(text_area.get('1.0', END), encode_image))
    showinfo('Encode', 'Encoding Complete\n' + str(encode_image.image_types()))

def decode_button_command(right_image, text_area, decode_variable):
    if decode_variable.get() == 'Text Area':
        text_area.delete('1.0', END)
        text_area.insert(END, decode_text(decode_image_filename))
    else:
        message = decode_text(decode_image_filename)
        new_filepath = askopenfilename()
        if new_filepath != () and new_filepath != '':
            with open(new_filepath, 'w') as new_file:
                new_file.write(message)
    showinfo('Decode', 'Decoding Complete')
