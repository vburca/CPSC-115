#
# File: recursion.py
# Author: Vlad Burca
#
# Created:  10/03/10
# Modified: 10/03/10
#


def countdown(n): 
  if n <= 0:
    print 'Blastoff!'
  else:
    print '*' * n
    countdown(n-1)

def start(n):
  if n <= 0: 
    print 'Start!'
  else:
    start(n-1)
    print '*' * n
    
def recursive_pattern(n):
  if n == 1 :
    print '*'
  else:
    print '*' * n
    recursive_pattern(n-1)
    print '*' * n

print
for i in range(5):
  print
  n = input(' Value of n: ')
  countdown(n)
print
print
for i in range(5):
  print
  n = input(' Value of n: ')
  start(n)
print
print
for i in range(5):
  print
  n = input(' Value of n: ')
  recursive_pattern(n)
