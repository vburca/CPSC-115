#
# File: turtle.py
# Author: Vlad Burca
#	  Jimmy Benjamin
# Lab Section: Wednesday
# 
# Created:       09/22/2010
# Last Modified: 09/22/2010
#
# TurtleWorld Exercises - Ch. 4.3 / 2
#

world.clear()
bob = Turtle(world)

def square(t,length):
'''
Draws a square of side 'length'. t is a turtle.
'''
 for i in range(1,5):
  fd(t,length)
  rt(t)

square(bob,20)
square(bob,50)
square(bob,100)
square(bob,150)
square(bob,200)
square(bob,300)
