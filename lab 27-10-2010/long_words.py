#
# File: long_words.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/27/2010
# Last Modified: 10/27/2010
#
# Exercise 1.2
#

f = open('crosswords.txt')
for line in f:
    word = line.strip()
    if len(word)>20:
        print word

