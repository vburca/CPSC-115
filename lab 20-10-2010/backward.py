#
# File: backward.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/20/2010
# Last Modified: 10/20/2010
#
# Exercise 1.1
#

s = raw_input(' Enter a word: ')
l = len(s)
i = l - 1
print ' The letters of the word "' + s + '" are: '
while i >= 0:
    print s[i]
    i = i - 1