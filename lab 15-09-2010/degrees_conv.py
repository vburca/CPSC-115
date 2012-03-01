#
# File: degrees_conv.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       09/15/2010
# Last Modified: 09/15/2010
#

import math

print ' Degrees and Radians Convertor '
print ' 1. Degrees to Radians '
print ' 2. Radians to Degrees '
check = input (' Your choice: ')
while check != 1 and check != 2:
    print ' Check must equal 1 or 2. '
    check = input (' Your choice: ')
if check == 1 :
    deg = input (' The value of the angle, in DEGREES: ')
    rad = deg * math.pi / 180.0
    print ' The equivalent of ', deg,' DEGREES, in RADIANS, is: ', rad
else:
    rad = input (' The value of the angle, in RADIANS: ')
    deg = rad * 180.0 / math.pi
    print ' The equivalent of ', rad,' RADIANS, in DEGREES, is: ', deg

