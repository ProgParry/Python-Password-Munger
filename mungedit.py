#!/usr/bin/env python3

import hashlib
import argparse

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
arguments.add_argument("--read", type=str, help="File path for passwords to try")
arguments.add_argument("--hash", type=str, help="Input the hash you want to crack")
args = arguments.parse_args()
if args.read and args.hash:
    try:
        with open(args.read, "r") as file:
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
                    if hash == args.hash:
                        print(f"Password match: {word}")
                        found = True
                        break
                if found:
                    break
                else:
                    print("Not found for: " + line)
    except FileNotFoundError:
        print("File " + args.read + " not found")
    except Exception as e:
        print(f"Error: {e}")
