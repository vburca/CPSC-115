#
# File: coffee3.py
# Author: Vlad Burca
# Lab Section: Wednesday
# 
# Created:       09/29/2010
# Last Modified: 09/29/2010
#

def print_price_list(price, n):
  total_price = n * (price + 0.75) + 1.50
  disc_price = n* ((price - price * 5/100) + 0.75) + 1.50
  total_price = round(total_price,2)
  disc_price = round(disc_price,2)
  print ' ', n, '\t\t', total_price, '\t\t', disc_price

print " Welcome to Allysa's Coffee! "
price = input (" Enter today's price for one pound: ")
price = round(price,2)
print ' Price List for Bulk Purchases at ', price, ' dollars per pound.'
print ' Pounds \t Cost \t\t With 5% Discount'
for i in range(10):
    print_price_list(price,i+1)

