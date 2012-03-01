#
# File: three_n_plus_1.py
# Author: Vlad Burca
#
# Created:  10/06/10
# Modified: 10/06/10
#
# Problem Statement: Write an iterative and a recursive version of the 
#               three_n_plus_1 function and then run both of them for values of
#               n = 1, 2, ... , 10. Save the output.
# Description: The program uses the two functions, three_n_plus_1 (implemented
#               as an iterative function), and three_n_plus_1_r (implemented as
#               a recursive function) in order to print the steps of the 
#               Collatz Conjecture for values of n = 1, 2, ... , 10.
#


def three_n_plus_1(n):
# Outputs the steps of the Collatz Conjecture (iterative version).
  while n > 1:
    print n,
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3 * n + 1
  print n

def three_n_plus_1_r(n):
# Outputs the steps of the Collatz Conjecture (recursive version).
  if n == 1:
    print n
  else:
    print n,
    if n % 2 == 0:
      three_n_plus_1_r(n/2)
    else:
      three_n_plus_1_r(3*n+1)

print ' Collatz Conjecture for: '
print
for i in range(10):
  print ' n = ', (i+1)
  print ' Interative \t: ',
  three_n_plus_1(i+1)
  print ' Recursive \t: ',
  three_n_plus_1_r(i+1)
  print
