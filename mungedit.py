import hashlib
import sys
import argparse
import re

#password = input("Enter password: ")
letters = {
    "a" : ["A","@","4"],
    "b" : ["B","8"],
    "c" : ["C","("],
    "d" : ["D"],
    "e" : ["E","3"],
    "f" : ["F"],
    "g" : ["G","8","9"],
    "h" : ["H"],
    "i" : ["I","1","!"],
    "j" : ["J"],
    "k" : ["K"],
    "l" : ["L","1"],
    "m" : ["M"],
    "n" : ["N"],
    "o" : ["O","0"],
    "p" : ["P"],
    "q" : ["Q","9"],
    "r" : ["R"],
    "s" : ["S","$","5"],
    "t" : ["T","+","7"],
    "u" : ["U"],
    "v" : ["V"],
    "w" : ["W"],
    "x" : ["X"],
    "y" : ["Y","?"],
    "z" : ["Z"],
}

arguments = argparse.ArgumentParser(description="A program for generating munged passwords and checking their hashes")
#arguments.add_argument("Input")
arguments.add_argument("--read", type=ascii, help="File path for passwords to try")
arguments.add_argument("--hash", type=ascii, help="Input the hash you want to crack")
arguments.parse_args()
if arguments.read and arguments.hash:
    try:
        with open(arguments.read, "r") as file:
            found = False
            for line in file:
                munged=[line]
                count=0
                for char in line:
                    munged_copy = munged[:]
                    for x in letters.keys():
                        if char == x:
                            for y in letters[x]:
                                for thing in munged_copy:
                                    string = thing[:count] + y + thing[count + 1:]
                                    munged.append(string)
                            break
                    count+=1
                hash_munged = []
                for word in munged:
                    hash = hashlib.md5(word.encode('utf-8')).hexdigest()
                    if hash == arguments.hash:
                        print(f"Password match: {word}")
                        found = True
                        break
                if found:
                    break            
    except FileNotFoundError:
        print("File " + arguments.read + " not found")
    except Exception as e:
        print(f"Error: {e}")
