#
# File: exam1.py
# Author: Vlad Burca
#
# Created:  10/03/10
# Modified: 10/03/10
#


n = input(' What is the size of the class?   ')
print 
print ' Now enter the scores below.'
print
s = 0
for i in range(n):
  a = ' Student ' + str(i+1) + ':   '
  x = input(a)
  s = s + x
print
print ' The average is ', float(s)/n