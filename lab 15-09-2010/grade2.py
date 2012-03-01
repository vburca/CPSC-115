#
# File: grade2.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       09/15/2010
# Last Modified: 09/15/2010
#

e_1 = input ('Enter the score of Exam 1: ')
e1p = input ('How much is Exam 1 worth? ')
e_2 = input ('Enter the score of Exam 2: ')
e2p = input ('How much is Exam 2 worth? ')
e_f = input ('Enter the score of Final Exam: ')
efp = input ('How much is Final Exam worth? ')
final = e1p * e_1 + e2p * e_2 + efp * e_f
print 'Your course grade is: ', final, ' %'
