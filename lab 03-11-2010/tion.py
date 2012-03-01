#
# File: tion.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       11/03/2010
# Last Modified: 11/03/2010
#
# Exercise 1.2
#

def isaSuffix(word, suff):
    if word[len(word)-len(suff):] == suff:
        return True
    else:
        return False

def getSuffix(list, suff):
    suff_list = []
    for word in list:
        if isaSuffix(word, suff):
            suff_list.append(word)
    return suff_list
    

f = open('crosswords.txt')
list = []
for line in f:
    word = line.strip()
    list.append(word)
suff_list = getSuffix(list, 'om')
print " In the official list of crosswords, the list of words that contain 'tion'\
as a suffix is: \n ", suff_list