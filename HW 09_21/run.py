#
# File: run.py
# Author: Vlad Burca
#
# Created:  09/18/10
# Modified: 09/18/10
#

# Getting the start values
h_start = input ('Enter the hour of the start time: ')
m_start = input ('Enter the minute of the start time: ')
miles = input ('Enter the number of miles I will run at tempo: ')
# Determining the 12-hour period
if h_start >= 12:
    time_start = 'PM'
    if h_start != 12:
        h_start = h_start - 12
else:
    time_start = 'AM'
# Setting up the variables for computing the final hour
h = h_start
m = m_start
s = 0
m = m + 8 + 8
s = s + 15 + 15
m = m + 7 * miles
s = s + 12 * miles
if s >= 60:
    s = s - 60
    m = m + 1
if m >= 60:
    m = m - 60
    h = h + 1
time = time_start
# Determining the 12-hour period
if h > 12:
    h = h - 12
    if time == 'AM':
        time = 'PM'
else:
        time = 'AM'
# Printing "interface" for printing single digits minutes or seconds.
if m_start < 10:
    m_start = '0' + str(m_start)
if m < 10:
    m = '0' + str(m)
if s < 10:
    s = '0' + str(s)
# Output printing
print 'If I start at ', h_start,' : ', m_start,' ', time_start, ' and run ', miles, ' milies at tempo, then I will be home at ', h, ' : ', m, ' : ', s, ' ', time, ' .'