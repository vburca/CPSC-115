#
# File: re.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       11/03/2010
# Last Modified: 11/03/2010
#
# Exercise 1.2
#

def isaPrefix(word, pref):
    if word[0:len(pref)] == pref:
        return True
    else:
        return False

f = open('crosswords.txt')
no_words = 0
begin_with_re = 0
s_with_re = ''
ls_with_re = 0
l_with_re = ''
ll_with_re = 0
for line in f:
    word = line.strip()
    no_words = no_words + 1
    if isaPrefix(word, 're'):
        if ls_with_re > len(word) or ls_with_re == 0:
            ls_with_re = len(word)
            s_with_re = word
        if ll_with_re < len(word):
            ll_with_re = len(word)
            l_with_re = word
        begin_with_re = begin_with_re + 1

print ' In the official list of ', no_words, ' crosswords, ', \
begin_with_re, " words begin with 're'. The shortest such word is '", \
s_with_re, "' and the longest such word is '", l_with_re, "'. "
