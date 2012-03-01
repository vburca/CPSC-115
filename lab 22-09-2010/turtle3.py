#
# File: turtle.py
# Author: Vlad Burca
#	  Jimmy Benjamin
# Lab Section: Wednesday
# 
# Created:       09/22/2010
# Last Modified: 09/22/2010
#
# TurtleWorld Exercises - Ch. 4.3 / 3
#

world.clear()
bob = Turtle(world)

def polygon(t,n,l):
'''
Draws a polygon of n sides of length l. t is a turtle.
'''
 for i in range(n):
  fd(t,l)
  rt(t,360.0/n)

polygon(bob,5,20)
polygon(bob,5,50)
polygon(bob,5,100)
polygon(bob,5,150)
polygon(bob,5,200)
