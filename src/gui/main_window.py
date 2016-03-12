#!/usr/bin/python

from Tkinter import *
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

# This is the overall window
root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


root_pane = PanedWindow(root, orient=VERTICAL)
root_pane.pack(fill=BOTH, expand=1)

images_pane = PanedWindow(root_pane, bg = 'green')
left_image = Label(images_pane, text = 'Left image')
right_image = Label(images_pane, text = 'Right image')
images_pane.add(left_image)
images_pane.add(right_image)
root_pane.add(images_pane)

info_label = Label(root_pane, bg = 'yellow', text="info label pane")
root_pane.add(info_label)

bottom_pane = PanedWindow(root_pane)
root_pane.add(bottom_pane)

text_area = Text(bottom_pane)
bottom_pane.add(text_area)

def print_foo():
    print("foo")

button_pane = PanedWindow(bottom_pane, orient=VERTICAL)
bottom_pane.add(button_pane)
select_file_button = Button(button_pane, text = 'Select Text File', command = print_foo)
button_pane.add(select_file_button)
encode_decode_button = Button(button_pane, text = 'Encode/Decode', command = print_foo)
button_pane.add(encode_decode_button)


root.config(menu=menubar)
root.mainloop()

