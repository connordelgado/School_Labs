#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 3.4 - Python Code 
# File:       Lab_3.4.py
# Purpose:    Demonstrate ifthen statements
#######################################################

# This program will demonstrate how to use decision
# statements in Python

# This program determines if a bonus should be awarded

# The main function
def main():
    print('Welcome to the program')
    monthlySales = getSales() # gets sales
    isBonus(monthlySales)
    isDayOff(monthlySales)

# This function gets the monthly sales
def getSales():
    monthlySales = float(input('Enter the Monthly Sales $'))
    return monthlySales

# This function checks if a bonus is to be awarded
def isBonus(monthlySales):
    if monthlySales >=100000:
        print('You have earned a $5,000 bonus!!!')

# this function checks if a day off is to be awarded
def isDayOff(monthlySales):
    if monthlySales >=90000 * 1.25:
        print('Everyone has earned a day off!!!')

# calls main
main()
