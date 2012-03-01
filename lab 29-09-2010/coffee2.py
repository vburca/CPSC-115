#
# File: coffee2.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       09/29/2010
# Last Modified: 09/29/2010
#

def print_invoice (price, pounds):
  total_cost = pounds * (price + 0.75) + 1.50
  print ' With ', price, ' dollars a pound, the total for ', pounds, ' is '\
, total_cost, ' dollars.'

print " Welcome to Allysa's Coffee! "
price = input (" Enter today's price for one pound: ")
for i in range(3):
  pounds = input (" How many pounds for this order? ")
  print_invoice(price, pounds)

