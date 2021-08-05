#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 6.3 - Python Code loop practice
# File:       Lab_6-3.py
# Purpose:    Loop Practice
#######################################################

# the main function
def main():
    totalCounter = 0
    totalAge = 0
    averageAge = 0

    # A Basic For loop
    print('I will display the numbers 1 through 5.')
    for num in [1, 2, 3, 4, 5]:
        print(num)

    # The Second Counter code
    print('I will display the numbers 1 through 60.')
    for num in range(1, 61):
        print(num)

    # The Accumulator code
    print('Please enter numbers and I will give the total.')
    for counter in range(5):
        counter = int(input("Enter a number: "))
        totalCounter = totalCounter + counter
        total = totalCounter / 5
    print('The total is ', total)

    # The Average Age code
    number = int(input('How many ages do you want to enter: '))
    for counter in range(0, number):
        counter = int(input('Enter the age: '))
        totalAge = totalAge + counter
    averageAge = totalAge / number
    print('The Average Age is: ', averageAge)

#calls main
main()

