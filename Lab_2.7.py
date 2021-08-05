#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 2.7 - Python Code for Retail Tax
# File:       Lab_2.7.py
# Purpose:    Calculates taxes
#######################################################

# the main function
def main():
    print('Welcome to the total tax calculator program')
    print() # prints a blank line
    salesTotal = input_sales_total()
    countyTax = calc_county(salesTotal)
    stateTax = calc_state(salesTotal)
    totalTax = calc_total(stateTax, countyTax)
    print_info(salesTotal, countyTax, stateTax, totalTax)

# this function will input sales total    
def input_sales_total():
    salesTotal = input('Enter the total sales made $')
    salesTotal = float(salesTotal)
    return salesTotal

# this function will calculate county tax at 2%
def calc_county(salesTotal):
    countyTax = salesTotal * 0.02
    return countyTax

# this function will calculate state tax at 4%
def calc_state(salesTotal):
    stateTax = salesTotal * 0.04
    return stateTax

# this function will calculate the tax total
def calc_total(stateTax, countyTax):
    totalTax = stateTax + countyTax
    return totalTax

# this function will print county taxes, state taxes, the sales total,
# and the total taxes
def print_info(salesTotal, countyTax, stateTax, totalTax):
    print('The total sales made was $', salesTotal)
    print('The county tax is $', countyTax)
    print('The state tax is $', stateTax)
    print('The total tax amount is $', totalTax)
    
# calls main
main()
