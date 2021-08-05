#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: Week 12 Homework
# File:       9.1_lab.py
# Purpose:    Use Bubble Sort and Binary Search
#######################################################


# the main function
def main():

    # all the variables primed, size sets the size of the array
    size = 20
    names = [''] * size
    searchName = ""

    # calls the two mandatory functions
    getNames(names, size)
    bubble_sort(names, size)

    # start of while loop which checks if done or if if searching for a name
    while searchName != "done":

        # takes user input to find what they're looking for
        searchName = input("Enter a name to search for <or 'done' to exit>: ")

        # if statement checks if done or not
        if searchName != "done":

            # sets up the position and times searched to be used later
            position, times_searched = search_names(names, searchName)

            # checks position to see if it has a real place or not
            if position >= 0:
                # prints all the info
                print('Name Found: ', searchName)
                print('Position: ', position)
                print('Array Lookups: ', times_searched)
            # sets up the else for if the name isnt in the array
            else:
                print('Name not found')
                print('Array Lookups: ', times_searched)


# the function that gets all the names
def getNames(names, size):

    # prompts user to enter names
    print('Please Enter 20 names:')
    print()

    # checks how many entries have been put in until 20 have been hit
    for counter in range(0, size):
        names[counter] = input(str(counter + 1) + ': ')
        counter = counter + 1


# the function that starts the bubble sort
def bubble_sort(names, size):

    # checks how many objects in the array
    n = len(names)

    # checks for i in max size of the array sets variable swapped to false
    for i in range(size):
        swapped = False

        # sets size - i - 1, this is done so as the below if statement will
        # make it so that the last variable will always find its place
        # so this allows it to continue going after that happens
        for j in range(0, size-i-1):

            # if statement realligns where everything goes
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
                swapped = True

        # if there is nothing else to swap it ends with this
        if swapped is False:
            return

    # prints a statement followed by the list of names alphabetically
    print()
    print('The sorted names are: ')
    print()
    for i in range(len(names)):
        print(names[i])
        print()


# function that searches the names and checks position
def search_names(names, searchName):

    # initializes all the variables
    first = 0
    last = len(names) - 1
    position = -1
    size = len(names)
    times_searched = 0

    # while loop that checks the position in the array and acts accordingly
    while position < 0 and first <= last:
        times_searched = times_searched + 1
        # times searched counts how many times it loops to display later

        # sets variables to check for position within array
        mid = (first + last) // 2
        midValue = names[mid]

        # if statement to see if the array is in the middle position
        if midValue == searchName:
            position = mid

        # elif to check if the statement is lower that the mid and adjusts
        # the highest value to be the mid if it needs to be
        elif midValue > searchName:
            last = mid - 1

        # else statement to raise the minimum of the value is higher than
        # the mid value
        else:
            first = mid + 1

    # returns position and times searched to display later
    return position, times_searched

# calls the main function
main()
