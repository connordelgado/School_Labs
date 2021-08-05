#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 2.5 - Python Code and Variables
# File:       lab_2.5.py
# Purpose:    This program demonstrates how to use variables
#####################################################

# This program uses functions and variables

# The main function

def main():
    print('Welcome to the variable program')
    print() #prints a blank line

    name = inputName()
    age = inputAge()
    print('Hello', name)
    print('You are', age,'years old')

# this function inputs name data
def inputName():
    name = input('Enter your name: ')
    return name

# this function inputs age data
def inputAge():
    age = input('Enter your age: ')
    return age

# calls main
main()
