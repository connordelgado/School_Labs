#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: 9.2 - Python Code Data Charges
# File:       lab_9.2.py
# Purpose:    Calculate data overages
#######################################################

# the main module


def main():

    # initializes the variables
    endProgram = "no"

    # starts the loop to ensure program restarts as needed
    while endProgram == "no":

        # Initializes all the variables
        GBsAllowed = 0
        GBsUsed = 0
        totalDue = 0
        GBsOver = 0

        # Calls all the functions
        GBsAllowed = getAllowed(GBsAllowed)
        GBsUsed = getUsed(GBsUsed)
        totalDue, GBsOver = calcTotal(GBsAllowed, GBsUsed, totalDue, GBsOver)
        printData(GBsAllowed, GBsUsed, totalDue, GBsOver)

        # gives the user option to get out of program or enter new data
        endProgram = input("Do you want to end the program? Enter yes or no: ")

        # checks the variables
        while endProgram != "yes" and endProgram != "no":
            print("Please enter exactly 'yes' or 'no'")
            endProgram = input("Do you want to end the program? yes or no: ")


# module that gets the GBs Allowed


def getAllowed(GBsAllowed):
    # Calls for user to enter how
    GBsAllowed = int(input("How many GBs are you allowed to use?: "))

    # checks the variables entered
    while GBsAllowed < 10 or GBsAllowed > 50:
        print("Please enter GBs between 10 and 50 to comply with our max/min")
        GBsAllowed = int(input("How Many GBs are allowed?: "))
    return GBsAllowed

# module that gets the GBs Used


def getUsed(GBsUsed):

    GBsUsed = int(input("How many GBs did you use?: "))

    # checks the variables entered
    while GBsUsed < 0:
        print("Please enter GBs of at least 0")
        GBsUsed = int(input("How many GBs did you use?: "))
    return GBsUsed

# module that calculates the total


def calcTotal(GBsAllowed, GBsUsed, totalDue, GBsOver):
    extra = 0

    # instructions for if you didn't go over
    if GBsUsed <= GBsAllowed:
        totalDue = 74.99
        GBsOver = 0
        print("You were not over your GBs for the month!")
        return totalDue, GBsOver

    # instructions for if you did go over
    else:
        GBsOver = GBsUsed - GBsAllowed
        extra = GBsOver * 4.44
        totalDue = 74.99 + extra
        print("You were over your GBs by ", GBsOver)
        return totalDue, GBsOver

# module that shows all the entered data and bill due etc


def printData(GBsAllowed, GBsUsed, totalDue, GBsOver):
    print("---------------MONTHLY USE REPORT---------------")
    print("GBs allowed were ", GBsAllowed)
    print("GBs used were ", GBsUsed)
    print("GBs over were ", GBsOver)
    print("Total due is $", totalDue)

# calls the main module
main()
