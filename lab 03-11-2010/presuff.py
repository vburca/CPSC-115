#
# File: presuff.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       11/03/2010
# Last Modified: 11/03/2010
#
# Exercise 1.3
#

def isaPrefix(word, pref):
    if word[0:len(pref)] == pref:
        return True
    else:
        return False

def isaSuffix(word, suff):
    if word[len(word)-len(suff):] == suff:
        return True
    else:
        return False

def getPrefSuffs(list, pre, suff):
    suff_list = []
    for word in list:
        if isaSuffix(word, suff) and isaPrefix(word, pre):
            suff_list.append(word)
    return suff_list
    
f = open('crosswords.txt')
list = []
for line in f:
    word = line.strip()
    list.append(word)
pref = raw_input(' Required prefix: ')
suff = raw_input(' Required suffix: ')
presuff_list = getPrefSuffs(list, pref, suff)
print " In the official list of crosswords, the list of words that contain \
the prefix '", pref, "' and the suffix '", suff, "' is: \n", presuff_list