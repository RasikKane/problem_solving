"""
Program to create multiple enumerated folders
inputs: <folderNames.txt> [path to create folders] [enum_flag] [separator for enumerator]
Algorithm:
* read argument .txt file containing line-separated names of folder
* enumerate them and create folders
"""
import os
from tkinter import *
from tkinter import filedialog

# When file address is not absolute, file is searched in directory of this code
rel_prefix = './'
rel_postfix = '/'
# default variables in absence of stdin arguments
file_addr = ''
rel_dir_addr = ''
enum_flag = False
sep = '_'


def get_path(address, prefix=rel_prefix, postfix=rel_postfix):
    # open input text file file_address and store each line denoting folder name into a list using readlines()
    # enumerate the list and create folders using for loop
    if os.path.isabs(address):
        return address + postfix if os.path.isdir(address) else address
    else:
        return prefix + address


def make_folders(in_file, flag, separator, rel_folder_address, prefix):
    try:
        print(flag)
        if flag is True:
            for index, name in enumerate(in_file.readlines()):
                os.mkdir(get_path(rel_folder_address, prefix) + str(index) + separator + name.strip())
        else:
            for name in in_file.readlines():
                os.mkdir(get_path(rel_folder_address, prefix) + name.strip())
    except OSError as e:
        print(e)


# driver code
def driver():
    global file_addr, enum_flag, sep, rel_dir_addr
    try:
        print(file_addr, rel_dir_addr)
        if not os.path.isfile(file_addr):
            raise IOError("Provide input file")
        else:
            file = open(get_path(file_addr, rel_prefix, rel_prefix))
            make_folders(file, enum_flag, sep, rel_dir_addr, rel_prefix)
    except IOError or FileNotFoundError as e:
        print(e)


def browse_button(open_item):
    # browse directory and set into variable
    global file_addr, rel_dir_addr
    if open_item is 'file':
        file_addr = filedialog.askopenfile().name
    if open_item is 'directory':
        rel_dir_addr = filedialog.askdirectory()


def set_flag(flag):
    global enum_flag
    enum_flag = flag


class App:

    def __init__(self, master):
        self.flag = BooleanVar()

        frame = Frame(master)
        frame.pack()

        self.file_button = Button(frame, text="input file", command=lambda: browse_button('file'))
        self.file_button.pack(side=LEFT)

        self.dir_button = Button(frame, text="destination folder", fg="red",
                                 command=lambda: browse_button('directory'))
        self.dir_button.pack(side=LEFT)

        self.enum_radio = Radiobutton(root, text="Enumerate", variable=self.flag, value=True,
                                      command=lambda: set_flag(self.flag.get()))
        self.enum_radio.pack(side=LEFT)

        self.make_dir = Button(frame, text="make directories", command=driver)
        self.make_dir.pack(side=LEFT)


root = Tk()
app = App(root)
root.mainloop()
