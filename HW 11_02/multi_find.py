#
# File: multi_find.py
# Author: Vlad Burca
#
# Created:  10/27/10
# Modified: 10/27/10
#
# Exercise 1.2
#

def my_find(seq, subseq, i, j):
    start = i
    finish = start + len(subseq)
    occ = []
    while finish <= j:
        if seq[start:finish] == subseq:
            occ.append(start)
        start = start + 1
        finish = finish + 1
    return occ

seq = raw_input(" The sequence: ")
subseq = raw_input(" The subsequence: ")
i = input(" The starting point of the search: ")
j = input(" The ending point of the search: ")

print ' All occurances of the provided subsequence: ', my_find(seq, subseq, i, j)