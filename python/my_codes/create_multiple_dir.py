"""
Program to create multiple enumerated folders
inputs: <folderNames.txt> [path to create folders] [enum_flag] [separator for enumerator]
Algorithm:
* read argument .txt file containing line-separated names of folder
* enumerate them and create folders
"""
import os
import sys

"""parse inputs to scripts"""
if not sys.argv:
    print("Provide input file")
    exit()

# When file address is not absolute, file is searched in directory of this code
rel_prefix = './'

# default variables in absence of stdin arguments
file_address = ''
rel_folder_address = ''
enum_flag = 1
sep = '_'

inputs = [file_address, rel_folder_address, enum_flag, sep]
for index, arg in enumerate(sys.argv[1:]):
    inputs[index] = arg

file_address, rel_folder_address, enum_flag, sep = inputs
enum_flag = int(enum_flag)
"""
open input text file file_address and store each line denoting folder name into a list using readlines()
enumerate the list and create folders using for loop
"""


def get_path(address, prefix):
    if os.path.isabs(address):
        return address
    else:
        return prefix + address


try:
    file = open(get_path(file_address, rel_prefix))

    try:
        if enum_flag:
            for index, name in enumerate(file.readlines()):
                os.mkdir(get_path(rel_folder_address, rel_prefix) + str(index) + sep + name.strip())
        else:
            for name in file.readlines():
                os.mkdir(get_path(rel_folder_address, rel_prefix) + name.strip())

    except OSError as e:
        print(e)

except FileNotFoundError as e:
    print(e)
    exit()
