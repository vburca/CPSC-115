#
# File: while_functions.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       10/13/2010
# Last Modified: 10/13/2010
#

# Pre: n is a positive integer [n > 0].
# Post: The sum of the first n positive numbers.
# Algorithm: Accumulate the sum of n + (n - 1) + (n - 2) + ... + 1  [while n > 0]
def sum(n):
    ''' Computes the sum of the first n positive integers for n > 0 '''
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s

# Pre: m and n are integers such that 0 < m <= n .
# Post: The sum of the integers between m and n (inclusively).
# Algorithm: Accumulate the sum of n + (n - 1) + (n - 2) + ... + m   [while n >= m].
def sum_range(m, n):
    ''' Computes the sum of the integers between m and n, for 0 < m <= n '''
    s = 0
    while m <= n:
        s = s + n
        n = n - 1
    return s
 
# Pre: x and n are integers such that n >= 0 .
# Post: The power of x to the n-th.
# Algorithm: Accumulate the product of x * x * x * x * ... * x  (n times), which is x^n.
def power(x, n):
    ''' Computes the x^n by accumulating the product of x * x * ... * x (n times) '''
    p = 1
    while n > 0:
        p = p * x
        n = n - 1
    return p

# Pre: no parameter.
# Post: The average value of the grades, if there is any grade != -1. Else, print an error.
# Algorithm: Get the sum of all the grades and then output the average value by dividing the
#            sum to the number of values (previously counted).
def exam_average():
    ''' Computes the average value of a given set of grades, until the grade given is '-1' '''
    s = 0
    n = 0
    gr = input(" Grade (type '-1' in order to stop): ")
    while gr != -1:    # while gr >= 0: 
        s = s + gr
        n = n + 1
        gr = input(" Grade (type '-1' in order to stop): ")
    if s != 0:
        print 
        print " The average of the grades: ", float(s)/n
    else:
        print " There are no grades to compute the average! "

# Pre: x and y are integers such that x > 0 and y > 0.
# Post: The greatest common divisor.
# Algorithm: Euclid's GCD Algorithm.
#            remainder <- x mod y
#            repeat while remainder != 0
#                   x <- y
#                   y <- remainder
#                   remainder <- x mod y
#            return y
def gcd(x, y):
    ''' Computes the greates common divisor of integers x and y using Euclid's GCD algorithm '''
    remainder = x % y
    while remainder != 0:
        x = y
        y = remainder
        remainder = x % y
    return y
  
print "While Functions:"
print
print "sum(n):"
n = input(" n = ")
print "sum(", n,") = ", sum(n)
print
print "sum_range(m, n):"
m = input(" m = ")
n = input(" n = ")
print "sum_range(", m,", ", n,") = ", sum_range(m, n)
print
print "power(x, n):"
x = input(" x = ")
n = input(" n = ")
print "power(", x,", ",n, ") = ", power(x, n)
print
print "exam_average() = "
exam_average()
print
print "gcd(x, y):"
x = input(" x = ")
y = input(" y = ")
print "gcd(", x, ", ", y, ") = ", gcd(x, y)