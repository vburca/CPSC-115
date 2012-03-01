#
# File: palindromes.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/27/2010
# Last Modified: 10/27/2010
#
# Exercise 1.3
#

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[len(s)-1] + reverse(s[0:len(s)-1])
    
def check_palindrome(s):
    s_r = reverse(s)
    if s == s_r:
        return True
    else:
        return False

f = open('crosswords.txt')
no_words = 0
no_palindromes = 0
ls_palindrome = 0
ll_palindrome = 0
l_palindrome = ''
s_palindrome = ''
for line in f:
    word = line.strip()
    no_words = no_words + 1
    if check_palindrome(word):
        no_palindromes = no_palindromes + 1
        if ls_palindrome == 0:
            ls_palindrome = len(word)
            s_palindrome = word
        if len(word) > ll_palindrome:
            ll_palindrome = len(word)
            l_palindrome = word
        elif len(word) < ls_palindrome:
            ls_palindrome = len(word)
            s_palindrome = word

print ' In the official list of ', no_words, ' crosswords, there are ', \
no_palindromes, " palindromes. The shortest palindrome is '", s_palindrome, "' and the \
longest palindrome is '", l_palindrome, "'. "