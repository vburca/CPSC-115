#
# File: no_e_words.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/27/2010
# Last Modified: 10/27/2010
#
# Exercise 1.4
#
  
def has_no_e(s):
    for c in s:
        if c == 'e':
            return False
    return True

f = open('crosswords.txt')
no_words = 0
no_noe = 0
ls_noe = 0
ll_noe = 0
l_noe = ''
s_noe = ''
for line in f:
    word = line.strip()
    no_words = no_words + 1
    if has_no_e(word):
        no_noe = no_noe + 1
        if ls_noe == 0:
            ls_noe = len(word)
            s_noe = word
        if len(word) > ll_noe:
            ll_noe = len(word)
            l_noe = word
        elif len(word) < ls_noe:
            ls_noe = len(word)
            s_noe = word

print ' In the official list of ', no_words, ' crosswords, there are ', \
no_noe, " that do not have 'e'. The shortest such word is '", \
s_noe, "' and the longest such word is '", \
l_noe, "'. "