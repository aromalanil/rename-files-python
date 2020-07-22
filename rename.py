# Python script to remove a keyword from every filenames in a directory
import os

files_and_folders = os.listdir()
files = list(filter(os.path.isfile, files_and_folders))
key = input("Enter word to remove : ")

for file in files:
    [filename, extension] = os.path.splitext(file)
    new_filename = filename.replace(key, '')
    os.replace(file, new_filename+extension)