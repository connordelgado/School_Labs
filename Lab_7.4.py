#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 7.4 - Programming Challenge 1 - Math Test
# File:       Lab_7.4.py
# Purpose:    Generate a simple math test
#######################################################

import random

# the main function
def main():
    print
    # initialize variables
    counter = 0
    studentName = 'NO NAME'
    averageRight = 0
    right = 0
    number1 = 0
    number2 = 0

    # call to input names
    studentName = inputNames()

    # while loop to run program again
    while counter < 10:
        # initializes variables
        number1, number2 = getNumbers()
        answer = getAnswer(number1, number2)
        right = checkAnswer(number1, number2, answer, right)
        counter = counter + 1

        #end of while loop
        print

    averageRight = results(right, averageRight)
    displayInfo(right, averageRight, studentName)

# this function gets the players names
def inputNames():
    studentName = input('Enter Student Name: ')
    return studentName

def getNumbers():
    number1 = random.randint(1, 500)
    number2 = random.randint(1, 500)

    return number1, number2

def getAnswer(number1, number2):
    print('What is the answer to the following equation?')
    print(number1)
    print('+')
    print(number2)
    answer = int(input('What is the sum: '))
    return answer

def checkAnswer(number1, number2, answer, right):
    if answer == number1 + number2:
        print('Right')
        right = right + 1

    else:
        print('Wrong')

    return right

def results(right, averageRight):
    averageRight = float(right) / 10
    return averageRight

def displayInfo(right, averageRight, studentName):
    print
    print('Information for students: ', studentName)
    print('The number right: ', right)
    print('The average right is ', averageRight, 'or', averageRight * 100,'%')

main()
