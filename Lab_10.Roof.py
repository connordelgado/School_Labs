#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 9.5 - Green Rooftop
# File:       lab_10.roof.py
# Purpose:    Show cost savings of a green roof
#######################################################


# the main function
def main():

    # initializes endProgram to no
    endProgram = 'no'
    print()

    notGreenCost = [0] * 12
    goneGreenCost = [0] * 12
    savings = [0] * 12
    
    while endProgram == 'no':
        print()

        # declare variables and initialize them
        
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October',
                  'November', 'December']
        option = 1

        # prints all options for user
        print('Enter 1 to enter new data')
        print('Enter 2 to display to the screen')
        print('Enter 3 to write savings to the file')
        print('Enter 4 to read savings from the file')

        # prompts user to find out what they want to do
        option = input('Enter option now: ')

        # option 1
        if option == '1':

            # calls functions to enter data
            getNotGreen(notGreenCost, months)
            getGoneGreen(goneGreenCost, months)
            energySaved(notGreenCost, goneGreenCost, savings)

        # option 2
        elif option == '2':

            # calls function to display data
            displayInfo(notGreenCost, goneGreenCost, savings, months)

        # option 3
        elif option == '3':

            # calls function to write file
            writeToFile(months, savings)

        # option 4
        elif option == '4':

            # calls function to read file
            readFromFile(months, savings)

        # prompts the user to see if they want to end the program
        endProgram = input('Do you want to end program? (Enter yes or no): ')

        # checks for bad input
        while not (endProgram == 'yes' or endProgram == 'no'):
            print('Please enter a yes or no')
            endProgram = input("Do you want to end program?(Enter yes or no):")


# the writeToFile Function
def writeToFile(months, savings):

    # opens the file for savings
    outFile = open('savings1.txt', 'a')
    print(outFile, 'Savings')

    counter = 0

    # writes all the savings for each month
    while counter < 12:

        outFile.write(months[counter] + '\n')
        outFile.write(str(savings[counter]) + '\n')
        counter = counter + 1

    # closes file after
    outFile.close()


# the readFromFile function
def readFromFile(months, savings):

    # opens the file
    inFile = open('savings1.txt', 'r')

    # reads and prints all the stats
    str1 = inFile.read()
    print(str1)
    months = inFile.read()
    print(months)
    savings = inFile.read()
    print(savings)
    inFile.close()

# the getNotGreen Function
def getNotGreen(notGreenCost, months):
    
    print()
    counter = 0

    # gets the users input for 12 months worth of energy costs original
    while counter < 12:
        print('Enter Not Green energy costs for', months[counter])
        notGreenCost[counter] = int(input('Enter now --> '))
        counter = counter + 1


# the getGone Green Function
def getGoneGreen(goneGreenCost, months):

    print()
    counter = 0

    # gets user input for 12 months worth of enery costs gone green
    while counter < 12:
        print('Enter Gone Green energy costs for', months[counter])
        goneGreenCost[counter] = int(input('Enter now --> '))
        counter = counter + 1


# the energySaved Function
def energySaved(notGreenCost, goneGreenCost, savings):
    print()
    counter = 0
    while counter < 12:
        savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
        counter = counter + 1


# the display info function
def displayInfo(notGreenCost, goneGreenCost, savings, months):

    counter = 0

    # sets up for all the info in the array to be printed
    print()
    print('                          Savings                          ')
    print('-----------------------------------------------------------')
    print('Savings       Not Green     Gone Green      Month     ')
    print('-----------------------------------------------------------')

    # makes the program print all the info in a visually pleasing way
    while counter < 12:
        print()
        print('$', savings[counter], '       $', notGreenCost[counter],
              '       $', goneGreenCost[counter], '         ', months[counter])
        counter = counter + 1
        print()

# calls the main function
main()
