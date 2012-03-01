#
# File: turtle.py
# Author: Vlad Burca
#	  Jimmy Benjamin
# Lab Section: Wednesday
# 
# Created:       09/22/2010
# Last Modified: 09/22/2010
#
# TurtleWorld Exercises - Ch. 4.3 / 1
#

world.clear()
bob = Turtle(world)

def square(t):
'''
Draws a square of side 100. t is a turtle.
'''
 for i in range(1,5,1):
  fd(t,100)
  rt(t)

square(bob)
