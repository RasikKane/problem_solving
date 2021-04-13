"""
Program to create multiple enumerated folders
inputs: <folderNames.txt> [relative path to create folders] [enumerator flag] [seperator for enumerator]
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

file_address = None
rel_file_prefix = './'
rel_folder_address = './'
sep = '_'

inputs = [file_address, rel_folder_address, sep]
for index, arg in enumerate(sys.argv[1:]):
    inputs[index] = arg

file_address, rel_folder_address, sep = inputs


"""
open input text file file_address and store each line denoting folder name into a list using readlines()
enumerate the list and create folders using for loop
"""
try:
    if os.path.isabs(file_address):
        file = open(file_address)
    else:
        file = open(rel_file_prefix + file_address)

    try:
        for index, name in enumerate(file.readlines()):
            os.mkdir(rel_folder_address + str(index) + sep + name.strip())

    except OSError as e:
        print(e)

except FileNotFoundError as e:
    print(e)
    exit()