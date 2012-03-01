#
# File: maptopiglatin.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       11/03/2010
# Last Modified: 11/03/2010
#
# Exercise 1.4
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
    
def findFirstVowel(word):
    '''Returns the first vowel in word or -1 if no vowels'''
    i = 0
    vowels = 'aeiou'
    while i < len(word):
        if word[i] in vowels:
            return i
        i = i + 1
    return -1

def pigLatin(word):
    '''Converts word to Pig Latin and returns the result'''
    pigword = ""
    firstvowel = findFirstVowel(word)
    if firstvowel == 0:   # word begins with a vowel
        pigword = word + 'yay'
    else:
        pigword = word[firstvowel:] +  word[0:firstvowel] + 'ay'
    return pigword


def mapToPigLatin(list):
    pig_list = []
    for word in list:
        pig_word = pigLatin(word)
        pig_list.append(pig_word)
    return pig_list   

f = open('crosswords.txt')
list = []
for line in f:
    word = line.strip()
    list.append(word)
pref = raw_input(' Required prefix: ')
suff = raw_input(' Required suffix: ')
while pref != '' and suff != '':
    presuff_list = getPrefSuffs(list, pref, suff)
    pig_list = mapToPigLatin(presuff_list)
    print 
    print " In the official list of crosswords, the list of words (translated into\
    Pig Latin) that cointain the prefix '", pref, "' and the suffix '", suff, "'\
    is: \n", pig_list
    print 
    print '================================================='
    pref = raw_input(' Required prefix: ')
    suff = raw_input(' Required suffix: ')