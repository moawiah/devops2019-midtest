import os, sys

result_dict = {}

##check for arguments
if len(sys.argv) != 2:
    print("Usage: You should provide one argument, 1)Word to be searched")
    exit(1)

if sys.argv[1] != "":
    word = sys.argv[1]
else:
    print("Usage: Please enter a valid word to be searched!")
    exit(2)

##Parse the string letter by letter, if the letter does not exist --> add it with its first occurance
for idx, letter in enumerate(word):
    if letter not in result_dict:
        result_dict[letter] = idx


print(result_dict)



