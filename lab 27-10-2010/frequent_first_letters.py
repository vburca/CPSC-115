#
# File: frequent_first_letters.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/27/2010
# Last Modified: 10/27/2010
#
# Exercise 2.1
#

def has_ch(s,ch):
    for c in s:
        if c == ch:
            return True
    return False

f = open('crosswords.txt')
no_words = 0
frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for line in f:
    word = line.strip()
    no_words = no_words + 1
    frequency[ord(word[0]) - 97] = frequency[ord(word[0]) - 97] + 1     
print ' In the official list of ', no_words, ' crosswords,'
max_freq = 0
maxc_freq = ''
for i in range(len(frequency)):
    if max_freq < frequency[i]:
        max_freq = frequency[i]
        maxc_freq = chr(i+97)
for i in range(len(frequency)):
    print frequency[i], " words begin with '", chr(i+97), "' ,"
print "and '", maxc_freq, "' is the most frequently-used first letter."