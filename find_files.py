# !/usr/bin/python3
import os, sys

path = ""
worksheet = []
file_count = 0

if len(sys.argv) != 3:
    print("Usage: You should provide two arguments, 1)path to be scanned 2)Word to be searched")
    exit(1)

if  os.path.isdir(sys.argv[1]):
    path = sys.argv[1]
else:
    print("Usage: Please enter a valid file path to be used for scanning!")
    exit(1)

if sys.argv[2] != "":
    word = sys.argv[2]
else:
    print("Usage: Please enter a valid word to be searched!")
    exit(2)

def find_files():
    for root, dirs, files in os.walk(path, topdown = True):
      for idx, name in enumerate(files):
          record = (os.path.join(root, name))
          ##TODO: I assumed that the files are not too large to be read into strings
          if word in open(record).read():
            print(record)


find_files()
