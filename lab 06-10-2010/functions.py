#
# File: functions.py
# Author: Vlad Burca
#         Trang Luong
# Lab Section: Wednesday
# 
# Created:       10/06/2010
# Last Modified: 10/06/2010
#

# Pre: n >= 1.
# Post: The sum of 1..n will be returned.
# Algorithm: Accumulates the sum of 0 + 1 + 2 + .. + n
def sum(n):
    # Computes the sum 1..n for n >= 1. (iterative)
    s = 0
    for i in range(n):
        s = s + (i + 1)
    return s

# Pre: n >= 1.
# Post: The sum of 1..n will be returned.
# Algorithm: Implements the following recursive definition:
#       When n == 1 return 1
#       Sum of 1..n = n + sum of (n-1)
def sum_r(n):
    # Computes the sum 1..n for n >= 1. (recursive)
    if n == 1:
        return 1
    else:
        return n + sum_r(n-1)

# Pre: 0 >= m > n.
# Post: The sum of m..n will be returned.
# Algorithm: Accumulates the sum of 0 + m + (m+1) + ... + n
def sum_range(m,n):
    # Computes the sum m..n for 0 >= m > n. (iterative)
    s = 0
    for i in range(m,n+1):
        s = s + i
    return s

# Pre: 0 >= m > n.
# Post: The sum of m..n will be returned.
# Algorithm: Implements the following recursive definition:
#       When n == m return m
#       Sum of m..n = n + sum of (m,n-1)
def sum_range_r(m,n):
    # Computes the sum m..n for 0 >= m > n. (recursive)
    if n == m:
        return m 
    else: 
        return n + sum_range_r(m,n-1)

# Pre: n >= 0.
# Post: The power x^n will be returned.
# Algorithm: Accumulates the product x^n = x * x * ... * x
def power(x,n):
    # Computes the x^n for n >= 0. (iterative)
    p = 1
    for i in range(n):
        p = p * x
    return p

# Pre: n >= 0.
# Post: The power x^n will be returned.
# Algorithm: Implements the following recursive definition:
#       When n == 1 return x
#       Computes x^n = x * x^(n-1)
def power_r(x,n):
    # Computes the x^n for n >= 0. (recursive)
    if n == 0:
        return 1
    else:
        return x * power_r(x,n-1)

print ' Sum Functions: '
n = input (' n = ')
print ' sum(', n,') = ', sum(n)
print ' sum_r(', n,') = ', sum_r(n)
print 
print ' Sum Range Functions: '
m = input (' m = ')
n = input (' n = ')
print ' sum_range(', m,',', n,') = ', sum_range(m,n)
print ' sum_range_r(', m,',', n,') = ', sum_range(m,n)
print
print ' Power Functions: '
x = input (' x = ')
n = input (' n = ')
print ' power(', x,',', n,') = ', power(x,n)
print ' power_r(', x,',', n,') = ', power_r(x,n)