#
# File: reverse.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/20/2010
# Last Modified: 10/20/2010
#
# Exercise 1.3
#

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[len(s)-1] + reverse(s[0:len(s)-1])

str1 = raw_input(' Enter your string: ')
str2 = reverse(str1)
print ' The reversed string of "' + str1 + '" is: ', str2