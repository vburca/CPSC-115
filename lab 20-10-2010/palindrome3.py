#
# File: palindrome3.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/20/2010
# Last Modified: 10/20/2010
#
# Exercise 2.3
#

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[len(s)-1] + reverse(s[0:len(s)-1])
    
def get_letters(s):
    l = len(s)
    s1 = ''
    for i in range(l):
        if str.isalpha(s[i]):
#        if s[i] != " " and s[i] != ',' and s[i] != '.' and \
#           s[i] != ';' and s[i] != ':' and s[i] != "'":
            s1 = s1 + s[i]
    return s1
    
t = raw_input(' Enter a word in lower-case letters: ')
aux = t.lower()
s1 = get_letters(aux)
s2 = reverse(s1)
if s1 == s2:
    print ' The word "' + t + '" is a palindrome. '
else:
    print ' The word "' + t + '" is not a palindrome. '