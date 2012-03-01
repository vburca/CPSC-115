#
# File: coffee1.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       09/29/2010
# Last Modified: 09/29/2010
#

print " Welcome to Allysa's Coffee! "
price = input (" Enter today's price for one pound: ")
pounds = input (" How many pounds for this order? ")
total_cost = pounds * (price + 0.75) + 1.50
print ' With ', price, ' dollars a pound, the total for ', pounds, ' is ', total_cost, ' dollars.'