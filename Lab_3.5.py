#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 3.5 - Python Code 
# File:       Lab_3.5.py
# Purpose:    Tests knowledge of ifthen statements
#######################################################

# This program gets guesses for different values and
# returns messages if guessed correctly

# The main function
def main():
    print('Welcome to the program')
    # All local variables
    age = getAge() # gets age
    weight = getWeight() # gets weight
    birthMonth = getMonth() # gets month
    # All Function Calls
    correctAnswers(age, weight, birthMonth)

# This function gets the user's guess for age
def getAge():
    age = float(input('Enter the guess for age: '))
    return age

# This function gets the user's guess for weight
def getWeight():
    weight = float(input('Enter the guess for weight: '))
    return weight

# This function gets the user's guess for birth month
def getMonth():
    birthMonth = input('Enter the guess for birth month: ')
    return birthMonth

# this function checks if given answers were correct
def correctAnswers(age, weight, birthMonth):
    if age <= 25:
        print('Congratulations, the age is 25 or less.')
    if weight >= 128:
        print('Congratulations, the weight is 128 or more.')
    if birthMonth == 'April':
        print('Congratulations, the birth month was April!')

# calls main
main()
