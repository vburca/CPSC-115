#
# File: exam2.py
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
nr_A = 0
nr_B = 0
nr_C = 0
nr_D = 0
nr_F = 0
for i in range(n):
  a = ' Student ' + str(i+1) + ':   '
  x = input(a)
  s = s + x
  if x >= 90:
    nr_A = nr_A + 1
  elif x >= 80:
    nr_B = nr_B + 1
  elif x >= 70: 
    nr_C = nr_C + 1
  elif x >= 60:
    nr_D = nr_D + 1
  else:
    nr_F = nr_F + 1
print
print ' The average is ', float(s)/n
print
print " There are ", nr_A, " A's."
print " There are ", nr_B, " B's."
print " There are ", nr_C, " C's."
print " There are ", nr_D, " D's."
print " There are ", nr_F, " F's."
