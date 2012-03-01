#
# File: fuel_cost.py
# Author: Vlad Burca
#
# Created:  09/23/10
# Modified: 09/23/10
#

def print_cost(miles, cost_gallon, epa):
    
    '''The formula to find out the total cost is given with respect to the MPG formula 
    Miles Per Gallon. Moreover, I use the division as a float number in order to
    manage all the possible values for 'miles' and 'epa' (e.g. when miles < epa).
    '''
    
    total_cost = ( float( miles ) / epa ) * cost_gallon
    print 'Your total cost is ', total_cost, ' dollars.'
    print 

# 'no' is a string used in order to properly print out the request for the variables.

no = ['st', 'nd', 'rd']
for i in range(3):
    p = 'Enter the distance traveled for the ' + str(i+1) + str(no[i]) + ' trip (in miles): '
    miles = input(p)
    q = 'Enter the cost of a gallon of gas for the ' + str(i+1) + str(no[i]) + ' trip (in dollars): '
    cost_gallon = input(q)
    r = 'Enter the EPA mileage rating for the ' + str(i+1) + str(no[i]) + ' trip (in MPG): '
    epa = input(r)
    print_cost(miles, cost_gallon, epa)
