#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 10-3 - Blood Drive
# File:       lab_10.3.py
# Purpose:    blood drive
#######################################################


# the main function
def main():

    endProgram = 'no'
    print
    while endProgram == 'no':
        option = 0
        print
        print('Enter 1 to enter in new data and store to file')
        print('Enter 2 to display data from the file')
        option = input('Enter Now -> ')
        print

        # declare variables
        pints = [0] * 7
        totalPints = 0
        averagePints = 0

        if option == '1':

            # function calls
            pints = getPints(pints)
            totalPints = getTotal(pints, totalPints)
            averagePints = getAverage(totalPints, averagePints)
            writeToFile(averagePints, pints)

        else:

            readFromFile(averagePints, pints)
            counter = 0
            for counter in range(6):
                outFile.write(str(pints[counter]) + '\n')
                outFile.write('Average Pints')
                outFile.write(str(averagePints) + '\n\n')
                outFile.close

        endProgram = input('Do you want to end program? (Enter no or yes):')
        while not (endProgram == 'yes' or endProgram == 'no'):
            print('Please enter a yes or no')
            endProgram = input('Do you want to end program? (Enter no or yes):')


# the getPints Function
def getPints(pints):

    counter = 0

    while counter < 7:
        pints[counter] = int(input('Enter pints collected: '))
        counter = counter + 1

    return pints


# the getTotal Function
def getTotal(pints, totalPints):

    counter = 0

    while counter < 7:

        totalPints = totalPints + pints[counter]
        counter = counter + 1

    return totalPints


# the getAverage function
def getAverage(totalPints, averagePints):

    averagePints = float(totalPints) / 7

    return averagePints


# the writeToFile function
def writeToFile(averagePints, pints):
    outFile = open('blood.txt', 'a')
    print(outFile, 'Pints Each Hour')

    for counter in range(6):
        outFile.write(str(pints[counter]) + '\n')
        outFile.write('Average Pints' + '\n')
        outFile.write(str(averagePints) + '\n\n')
        outFile.close


# the readFromFile function
def readFromFile(averagePints, pints):

    inFile = open('blood.txt','r')
    str1 = inFile.read()
    print(str1)
    for counter in range(6):
        pints[counter] = inFile.read()
        str2 = inFile.read()
        print(str2)
        averagePints = inFile.read()
        print(averagePints)
        

# calls main
main()
