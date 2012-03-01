#
# File: grade1.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       09/15/2010
# Last Modified: 09/15/2010
#

e1 = input ('Enter the score of Exam 1: ')
e2 = input ('Enter the score of Exam 2: ')
e_f = input ('Enter the score of Final Exam: ')
final = 0.3 * e1 + 0.3 * e2 + 0.4 * e_f
print 'Your course grade is: ', final, '%'
