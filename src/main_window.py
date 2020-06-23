#!/usr/bin/python

import _tkinter
from tkinter import *
from PIL import Image, ImageTk
#from tkMessageBox import *
from button_commands import *

##################################################
# Sets up the main window frame with the title   #
# and the grid system                            #
##################################################
master = Tk()

master.wm_title('Steganography')
master.columnconfigure(0, weight=2)
master.columnconfigure(1, weight=1)
master.columnconfigure(2, weight=1)
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)

##################################################
# Labels to display the images in, when clicked, #
# opens dialogs to set up to encode or decode    #
# that image.                                    #
##################################################
left_image_filename = StringVar()
right_image_filename = StringVar()
left_image_filename.set('')
right_image_filename.set('')

left_image = Label(master, text='Open File to kickoff',
                   anchor=W, justify=LEFT, wraplength=200, cursor='hand1')
left_image.grid(row=0, column=0, sticky=W+E+N+S)

right_image = Label(master, text='',
                    anchor=W, justify=LEFT, wraplength=200, cursor='hand1')
right_image.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)

left_image.bind('<Button-1>', lambda e: open_encode_image(left_image, right_image, left_image_filename))
right_image.bind('<Button-1>', lambda e: open_decode_image(right_image, left_image, right_image_filename))

##################################################
# Text area to display or load in text to or     #
# from the image                                 #
##################################################
text_area = Text(master, height=10, width=50)
text_area.grid(row=2, column=0, rowspan=3, sticky=W+E+N+S)

##################################################
# lableframes to hold the radio buttons. The     #
# raido buttons select if the text should input  #
# output from a file or the text box.            #
##################################################
encode_lableframe = LabelFrame(master, text='Encode Input')
encode_lableframe.grid(row = 2, column = 1, columnspan=2, sticky=W+E+N+S)

encode_variable = StringVar()
encode_variable.set('Text Area')

encode_rb_1 = Radiobutton(encode_lableframe, text='Text Area',
                          variable=encode_variable, value="Text Area")
encode_rb_1.grid(row=0,column=0, sticky=W)

encode_rb_2 = Radiobutton(encode_lableframe, text='File',
                          variable=encode_variable, value="File",
                          command=lambda : read_text(text_area, encode_variable))
encode_rb_2.grid(row=1,column=0, sticky=W)

decode_variable = StringVar()
decode_variable.set('Text Area')
decode_lableframe = LabelFrame(master, text='Decode Output')
decode_lableframe.grid(row = 3, column = 1, columnspan=2, sticky=W+E+N+S)

decode_rb_1 = Radiobutton(decode_lableframe, text='Text Area',
                          variable=decode_variable, value="Text Area")
decode_rb_1.grid(row=0,column=0, sticky=W)

decode_rb_2 = Radiobutton(decode_lableframe, text='File',
                          variable=decode_variable, value="File")
decode_rb_2.grid(row=1,column=0, sticky=W)

##################################################
# Buttons to act as the kickers for the whole    #
# process.                                       #
##################################################
encode_button = Button(master, text='Encode',
                       command=lambda: encode_button_command(left_image, right_image, text_area, left_image_filename, right_image_filename),
                       cursor='hand1')
encode_button.grid(row=4, column=1, sticky=W+E)

decode_button = Button(master, text='Decode',
                       command=lambda: decode_button_command(right_image, text_area, decode_variable, right_image_filename),
                       cursor='hand1')
decode_button.grid(row=4, column=2, sticky=W+E)

##################################################
# sets up the menubar. NOTE: this does not add   #
# the keybindings, thats below, in the bind.     #
##################################################
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='Read text from file', command=lambda: read_text(text_area, encode_variable))
filemenu.add_command(label='Open image to encode', command=lambda : open_encode_image(left_image, right_image, left_image_filename))
filemenu.add_command(label='Open image to decode', command=lambda : open_decode_image(right_image, left_image, right_image_filename))

helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label='How to use', command=how_to_use_command)
helpmenu.add_command(label='About', command=about_command)
helpmenu.add_command(label='Quit', command=lambda e:quit_command(), underline=0, accelerator='C-q')

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Help', menu=helpmenu)

master.bind('<Control-q>', lambda e=None: quit_command(master))
master.config(menu=menubar)

##################################################
# Starts the whole thing                         #
##################################################
mainloop()
