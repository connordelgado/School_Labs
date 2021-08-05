#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 5.5 - Yum Yum Burger Joint
# File:       Lab_5.5.py
# Purpose:    Burger Joint Program
#######################################################

# the main function
def main():
    # initialize variables
    endProgram = 'no'
    # Loop to run program again
    while endProgram == 'no':
        # resest variables
        totalBurger = 0
        totalFry = 0
        totalSoda = 0
        total = 0
        endOrder = 'no'
        # Loop to get order
        while endOrder == 'no':
            print("Enter 1 for Yum Yum Burger")
            print("Enter 2 for Grease Yum Burger")
            print("Enter 3 for Soda Yum")
            option = int(input("Enter now -> "))
            if option == 1:
                totalBurger = getBurger(totalBurger)
            elif option == 2:
                totalFry = getFry(totalFry)
            elif option == 3:
                totalSoda = getSoda(totalSoda)
            endOrder = input('Do you want to end your order? (yes/no): ')
        total = calcTotal(totalBurger, totalFry, totalSoda)
        printReceipt(total)
        endProgram = input('Do you want to end the program? (yes/no): ')
        
# This function gets inputs to get total burger count
def getBurger(totalBurger):
    burgerCount = int(input("Enter the number of burgers you want "))
    totalBurger = totalBurger + (burgerCount * .99)
    return totalBurger

# This function gets inputs to get total fry count
def getFry(totalFry):
    fryCount =int( input("Enter the number of fries you want "))
    totalFry = totalFry + (fryCount * .79)
    return totalFry

# This function gets inputs to get total soda count
def getSoda(totalSoda):
    sodaCount = int(input("Enter the number of sodas you want "))
    totalSoda = totalSoda + (sodaCount * 1.09)
    return totalSoda

# this function calculates the total using above counts
def calcTotal(totalBurger, totalFry, totalSoda):
    subtotal = totalBurger + totalFry + totalSoda
    tax = subtotal * .06 # current tax rate at .06
    total = subtotal + tax
    return total

# this function takes the total from above and prints receipt
def printReceipt(total):
    print("Your total is $", total)

# calls main function
main()
