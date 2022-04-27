// Description: Simulate an airline check-in system
//
// Course Name : C++ programming 2541
// course num: 272290
// Author: Connor Delgado
// Version: 1.1
// Date: 04/22/22

#include <iostream>
using namespace std;

// class callled Plane, pretty much holds the entire program
class Plane
{
    // private class type for first and econ as they're methods used entirely within the class.
    private:
       
       // first called when they select a first class ticket, adds 1 to counter and displays seat number
        void First()
        {
            firstClass++;
            cout << "You have selected seat #" << firstClass << " of 5." << endl;
            
        }

        // econ called when they select a economy class ticket, adds 1 to counter and displays seat number
        void Econ()
        {

            economyClass++;
            cout << "You have selected seat #" << economyClass << " of 5." << endl;

        }
    
    // public type declared for the ones used outside the class
    public:
        
        // initialize 2 variables for counters
        int firstClass;
        int economyClass;

        // check in method used, basically a menu
        void checkIn()
        {
            // initialize variable for menu choice
            int choice;

            // do while loop so it automatically runs once and will stop when firstClass and econClass = 5
            do
            {
                // prompt user for choice of ticket and get it
                cout << "Enter 1 to select First Class Seat (Choice: 1): " << endl;
                cout << "Enter 2 to select Economy Seat (Choice: 2): " << endl;
                cin >> choice;

                // if they select first call first
                if(choice == 1)
                {
                    // calls first
                    if (firstClass < 5)
                    {
                        First();
                    }

                    // if theres 5 firstClass it tells you there are no seats left
                    if (firstClass = 5)
                    {

                        cout << "No more seats available for this selection." << endl;

                    }

                }
                
                // if they select second call econ
                else if(choice == 2)
                {
                    // if there are less than 5 economy tickets calls econ
                    if (economyClass < 5)
                    {
                        
                        Econ();

                    }

                    // if there are 5 selected tells them they're out of tickets.
                    if (economyClass = 5)
                    {

                        cout << "No more seats available for this selection." << endl;

                    }

                }

                // validation rule in case of bad input
                else
                {

                    cout << "Try again..." << endl;

                }

                // if firstClass and economyClass are at 5 tickets it tells you the seats are all gone and breaks out of loop
                if(firstClass == 5 && economyClass == 5)
                {
                    cout << "All seats have been taken." << endl;
                    break;
                }

            }while(firstClass <= 5 && economyClass <= 5);   // while loop that goes until <=5 for both ticket types
        }

};

// main function
int main()
{
    // establishes class Plane as c
    Plane c;

    // initialize class c variables
    c.firstClass = 0;
    c.economyClass = 0;
    
    // call checkIn function from class Plane
    c.checkIn();

}