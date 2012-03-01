#
# File: time_examples.py
# Author: Vlad Burca
#
# Created:  11/09/10
# Modified: 11/09/10
#

from Time import Time

print "to_seconds(): "
print "------------- "
i = 1
while i <= 5:
    print i, "):"
    h = input("Number of initial hours: ")
    m = input("Number of initial minutes: ")
    s = input("Number of initial seconds: ")
    time1 = Time(h, m, s)
    print "Time ", time1, " to seconds: ", time1.to_seconds()
    i = i + 1
    print
print

print "from_seconds(): "
print "------------- "
i = 1
while i <= 5:
    print i, "):"
    time2 = Time()
    s = input("Number of seconds: ")
    time2.from_seconds(s)
    print "From ", s, " seconds, time: ", time2
    i = i + 1
    print
print 

print "s_increment(): "
print "------------- "
i = 1
while i <= 5:
    print i, "):"
    h = input("Number of initial hours: ")
    m = input("Number of initial minutes: ")
    s = input("Number of initial seconds: ")
    time3 = Time(h, m, s) 
    inc = input ("Number of seconds to increment: ")
    print "Time ", time3,
    time3.s_increment(inc)
    print " incremented by ", inc, " seconds: ", time3
    i = i + 1
    print
print

print "difference(): "
print "------------- "
i = 1
while i <= 5:
    print i, "):"
    print "Start time: "
    h = input("Number of initial hours: ")
    m = input("Number of initial minutes: ")
    s = input("Number of initial seconds: ")
    start_time = Time(h, m, s)
    print "Finish time: "
    h = input("Number of initial hours: ")
    m = input("Number of initial minutes: ")
    s = input("Number of initial seconds: ")
    finish_time = Time(h, m, s)
    time_difference = start_time.difference(finish_time)
    print "The difference between ", start_time, " and ", finish_time,\
          " : ", time_difference
    i = i + 1
    print
print
