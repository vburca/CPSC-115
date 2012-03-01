#
# File: my_find.py
# Author: Vlad Burca
#
# Created:  10/27/10
# Modified: 10/27/10
#

def my_find(seq, subseq, i, j):
    start = i
    finish = start + len(subseq)
    while finish <= j:
        if seq[start:finish] == subseq:
            return start
        start = start + 1
        finish = finish + 1
    return -1

seq = raw_input(" The sequence: ")
subseq = raw_input(" The subsequence: ")
i = input(" The starting point of the search: ")
j = input(" The ending point of the search: ")

print ' The lowest start index of the given subsequence is: ', my_find(seq, subseq, i, j)
