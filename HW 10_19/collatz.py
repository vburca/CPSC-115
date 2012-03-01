#
# File: collatz.py
# Author: Vlad Burca
#
# Created:  10/06/10
# Modified: 10/06/10
#
# Problem Statement: 2.1 Using either your recursive or iterative version of the
#           function three_n_plus_1(), write a Python script, including whatever
#           functions you need, to find the high water marks for the following 
#           ranges of integers: n < 100, n < 1000, n < 10000, n < 100000,
#           n < 1000000.
# Description: The program computes the high water marks of specific intervals 
#           for the Collatz Conjecture.
#


def three_n_plus_1_r(n):
# Counts the steps of the Collatz Conjecture for integer n.
  if n == 1:
    return 0             # Returns 0 in order to not count reaching to '1' as a step.
  else:
    if n % 2 == 0:
      return 1 + three_n_plus_1_r(n/2)
    else:
      return 1 + three_n_plus_1_r(3*n+1)

max_steps = 0
bound = 100
for k in range(1000000):
  if k + 1 == bound:
    print ' For n <', bound, ' the high water mark is', n, ' with a stopping time of', \
    max_steps, '. '
    bound = bound * 10
  steps = three_n_plus_1_r(k+1)
  if steps > max_steps:
    max_steps = steps
    n = k + 1
