#
# File: turtle.py
# Author: Vlad Burca
#	  Jimmy Benjamin
# Lab Section: Wednesday
# 
# Created:       09/22/2010
# Last Modified: 09/22/2010
#
# TurtleWorld Exercises - Ch. 4.3 / 5
#

#
# File: turtle.py
# Author: Vlad Burca
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

def polyline(t, n, length, angle):
    """Draw n line segments with the given length and
    angle (in degrees) between them.
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
'''
Draws an arc of radius r and angle 'angle'. t is a turtle.
'''
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before the polyline reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

arc(bob,50,100)
