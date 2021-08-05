#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400 Feb 5 2021
# Assignment: Lab 1-5 seasonAverages
# File:       Lab1-5.py
# Purpose:    Provide the season average football record
#######################################################

print('\n**  Connor Delgado  **\n')  # Display author's name

print('Football Season Win Average Calculator')
season1 = int(input('Enter Number of Wins Season 1. '))
season2 = int(input('Enter Number of Wins Season 2. '))
season3 = int(input('Enter Number of Wins Season 3. '))
season4 = int(input('Enter Number of Wins Season 4. '))
season5 = int(input('Enter Number of Wins Season 5. '))
seasonAverage = (season1 + season2 + season3 + season4 + season5) / 5
print('The Average number of wins was', seasonAverage)
