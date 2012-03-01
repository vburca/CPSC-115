#
# File: runner.py
# Author: Vlad Burca
#
# Created:  11/09/10
# Modified: 11/09/10
#


'''
I will run at tempo, 7 minutes and 12 seconds per mile,
determine the time I will get home. As before, assume that
I will run the first and last miles at an easy pace of 8 minutes
and 15 seconds per mile
'''

from Time import Time

h = input("Enter the hour of the start time: ")
m = input("Enter the minute of the start time: ")
s = 0
miles = input("Enter the number of miles I will run at tempo: ")
start_time = Time(h, m, s)
tempo = Time(0, 7, 12)
total_tempo_seconds = tempo.to_seconds() * miles
#tempo.from_seconds(total_tempo_seconds)
pace = Time(0, 8, 15)
total_pace_seconds = pace.to_seconds() * 2
#pace.from_seconds(total_pace_seconds)
total_StartTime_seconds = start_time.to_seconds()
finish_time = Time()
finish_time.from_seconds(total_StartTime_seconds + \
                                       total_pace_seconds + \
                                       total_tempo_seconds)
print "If I start at ", start_time, " and run ", miles, "\
miles at tempo, then I will be home at ", finish_time, ". "


