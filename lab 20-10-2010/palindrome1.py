#
# File: palindrome1.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/20/2010
# Last Modified: 10/20/2010
#
# Exercise 2.1
#

s1 = raw_input(' Enter a word in lower-case letters: ')
l = len(s1)
i = l - 1
s2 = ''
while i >= 0:
    s2 = s2 + s1[i]
    i = i - 1
if s1 == s2:
    print ' The word "' + s1 + '" is a palindrome. '
else:
    print ' The word "' + s1 + '" is not a palindrome. '