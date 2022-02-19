#!/usr/bin/env python

#import sys is for system variables
import sys
import re

#stdin = standard input
for line in sys.stdin:

    #strip white spaces at begining and end of line
    line = line.strip()

    #split each line up
    words = line.split()

    #remove numbers and special characters
    clean_words = re.sub('\W+','', words)

    #process each word and assign a value of 1 to each word
    # \t means tab
    for word in clean_words:
        print(word + "\t1")

#mapper - breaking up words into units

#echo 'a quick brown fox jumps over a lazy dog'|./mapper.py
