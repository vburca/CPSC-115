#
# File: turtle.py
# Author: Vlad Burca
#	  Jimmy Benjamin
# Lab Section: Wednesday
# 
# Created:       09/22/2010
# Last Modified: 09/22/2010
#
# TurtleWorld Exercises - Ch. 4.3 / 4
#

world.clear()
bob = Turtle(world)
bob.delay=0

import math

def polygon(t,n,l):
'''
Draws a polygon of n sides of length l. t is a turtle.
'''
 for i in range(n):
  fd(t,l)
  rt(t,360.0/n)

def circle(t,r):
'''
Draws a circle of radius r. t is a turtle.
'''
  l=1
  n=(2*math.pi*r)/l
  polygon(t,n,l)

circle(bob,75)
