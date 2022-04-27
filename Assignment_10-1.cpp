// Description: Read file and determine it's contents to determine certain file characteristics
//
// Course Name : C++ programming 2541
// course num: 272290
// Author: Connor Delgado
// Version: 1.1
// Date: 04/07/22

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// the main function, only one we'll need
int main()
{

    // Initialize all variables, need to count uppercase, lowercase, and total digits
    int uppercase = 0,      // to count uppercase
        lowercase = 0,      // to count lowercase
        digitCount = 0;     // to count digits
    char characters;        // used to check each character one by one

    // This opens the text.txt file for analysis
    ifstream text;
    text.open("text.txt");
    
    // this checks each character of the text document character by character
    while(text.get(characters))
    {
        // check if is uppercase
        if (isupper(characters))
        {
            uppercase = uppercase + 1;  // adds 1 if uppercase
        }

        // check if is lowercase
        if (islower(characters))
        {
            lowercase = lowercase + 1;  // adds 1 if lowercase
        }

        // check if is a digit
        if (isdigit(characters))
        {
            digitCount = digitCount + 1;    // adds 1 if a digit
        }
        
    }
    
    // close the text file
    text.close();
    
    // output the number of uppercase letters
    cout << "The total number of uppercase letters is " << uppercase << endl;

    // output the number of lowercase letters
    cout << "The total number of lowercase letters is " << lowercase << endl;
    
    // output the total digit count
    cout << "The total number of digits is " << digitCount << endl;

}