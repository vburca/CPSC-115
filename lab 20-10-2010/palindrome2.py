#
# File: reverse.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/20/2010
# Last Modified: 10/20/2010
#
# Exercise 2.2
#

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[len(s)-1] + reverse(s[0:len(s)-1])
    
s1 = raw_input(' Enter a word in lower-case letters: ')
s2 = reverse(s1)
if s1 == s2:
    print ' The word "' + s1 + '" is a palindrome. '
else:
    print ' The word "' + s1 + '" is not a palindrome. '