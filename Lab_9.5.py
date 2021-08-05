#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 9.5 - Green Rooftop
# File:       lab_9.5.py
# Purpose:    Show cost savings of a green roof
#######################################################


def main():
    endProgram = 'no'
    print()
    while endProgram == 'no':
        print()
        # declare variables
        notGreenCost = [0] * 12
        goneGreenCost = [0] * 12
        savings = [0] * 12
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October',
                  'November', 'December']
        getNotGreen(notGreenCost, months)
        getGoneGreen(goneGreenCost, months)
        energySaved(notGreenCost, goneGreenCost, savings)
        displayInfo(notGreenCost, goneGreenCost, savings, months)
        endProgram = input('Do you want to end program? (Enter yes or no): ')
        while not (endProgram == 'yes' or endProgram == 'no'):
            print('Please enter a yes or no')
            endProgram = input("Do you want to end program?(Enter yes or no):")


def getNotGreen(notGreenCost, months):
    print()
    counter = 0
    while counter < 12:
        print('Enter Not Green energy costs for', months[counter])
        notGreenCost[counter] = int(input('Enter now -->'))
        counter = counter + 1


def getGoneGreen(goneGreenCost, months):
    print()
    counter = 0
    while counter < 12:
        print('Enter Gone Green energy costs for', months[counter])
        goneGreenCost[counter] = int(input('Enter now -->'))
        counter = counter + 1


def energySaved(notGreenCost, goneGreenCost, savings):
    print()
    counter = 0
    while counter < 12:
        savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
        counter = counter + 1


def displayInfo(notGreenCost, goneGreenCost, savings, months):
    counter = 0
    print()
    print('                          Savings                          ')
    print('-----------------------------------------------------------')
    print('Savings       Not Green     Gone Green      Month     ')
    print('-----------------------------------------------------------')
    while counter < 12:
        print()
        print('$', savings[counter], '       $', notGreenCost[counter],
              '       $', goneGreenCost[counter], '         ', months[counter])
        counter = counter + 1
        print()

main()
