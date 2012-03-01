#
# File: rec_turtle2.py
# Author: Vlad Burca
#         Trang Luong
# Lab Section: Wednesday
# 
# Created:       10/06/2010
# Last Modified: 10/06/2010
#
# Description: Draws a flower using squares.
#

world.clear()
bob = Turtle(world)
bob.delay = 0

def square(t,l,n,angle):
 if n == 0: 
   pu(t)
 else:
   for i in range(1,5):
     fd(t,l)
     rt(t)
   lt(t,angle)
   square(t,l,n-1,angle)

square(bob,100,24,360.0/24)

