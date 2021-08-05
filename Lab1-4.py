#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400 Feb 5 2021
# Assignment: Lab 1-4 degreeAudit
# File:       Lab1-4.py
# Purpose:    Provide an Arbitrary Degree Audit
#######################################################

print('\n**  Connor Delgado  **\n')  # Display author's name

studentName = input('Enter student name. ')
degreeName = input('Enter degree name. ')
creditsDegree = int(input('Enter credits required for degree. '))
creditsTaken = int(input('Enter the total number credits taken. '))
creditsLeft = creditsDegree - creditsTaken
print('The student\'s name is', studentName)
print('The program requires', creditsDegree,
      'credits and they have taken', creditsTaken,
      'credits so far.')
print('You have ', creditsLeft, 'credits left to take until graduation.')
