#
# File: future_values.py
# Author: Vlad Burca
#
# Created:  09/25/10
# Modified: 09/25/10
#

def print_next_value(c_amount, i_rate):
    
    ''' This function has the purpose of computing the value of the investment using the
    interest rate and the current value of the investment. The function returns the new value 
    of the investment in order to be used for the next callings of it.
    '''
    
    amount = c_amount + c_amount * i_rate
    print ' After one year, your investment is worth ', amount, ' dollars.'
    return amount

c_amount = input (' Enter the initial value of an investment: ')
i_rate = input (' Enter an annual interest rate: ')
print_next_value(print_next_value(print_next_value(c_amount, i_rate), i_rate), i_rate)



'''

# This is just another way of implementing the code. Its purpose is to print the investment
# over time in a more clear, user-friedly way.

def print_next_value(c_amount, i_rate, x):
    amount = c_amount + c_amount * i_rate
    if x == 1:
        print ' After 1 year, your investment is worth ', amount, ' dollars.'
    else:
        if x > 1:
            print ' After ', x, ' years, your investment is worth ', amount, 'dollars.'
    return amount

years = 3
amount = c_amount
for i in range(years+1):
    amount = print_next_value(amount,i_rate,i)

'''