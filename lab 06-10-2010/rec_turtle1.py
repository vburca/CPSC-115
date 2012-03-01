#
# File: rec_turtle1.py
# Author: Vlad Burca
#         Trang Luong
# Lab Section: Wednesday
# 
# Created:       10/06/2010
# Last Modified: 10/06/2010
#
# Description: Draws nested squares.
#

world.clear()
bob = Turtle(world)
bob.delay = 0

# Function to initiate the turtle t in the right position. 
def init(t,n):
 pu(t)
 for i in range(600-n/5):
   bk(t)
 lt(t)
 for i in range(600-n/5):
   fd(t)
 rt(t)
 pd(t)

def jump(t,rate):
 pu(t)
 fd(t,rate)
 rt(t)
 fd(t,rate)
 lt(t)
 pd(t)

def square(t,n,rate):
 if n <= 0: 
   pu(t)
 else:
   for i in range(1,5):
     fd(t,n)
     rt(t)
   jump(bob,rate)
   square(t,n-2.0*rate,rate)


#init(bob,600)
square(bob,500,10)


