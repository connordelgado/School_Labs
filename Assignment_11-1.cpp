// Description: Simulate inventory bins in a warehouse
//
// Course Name : C++ programming 2541
// course num: 272290
// Author: Connor Delgado
// Version: 1.1
// Date: 04/12/22

#include <iostream>
#include <iomanip>
using namespace std;

// struct to hold inventory numbers string for bin type int for parts number
struct InventoryInfo
{
    
    std::string bin;
    int parts;

};

// call to add parts to the bin
void addParts(struct InventoryInfo inventoryList [10], int i)
{
    // initialize parts variable and array
    int addPart;
    
    // asks user how many parts to add
    cout << "How many parts are to be added to the bin?: ";
    cin >> addPart;

    // validation rule for negative number
    if(addPart <= - 1)
    {
        cout << "Can't add Negative Parts.";
    }

    // can't hold more than 30 parts, validates the math on this rule
    if(addPart + inventoryList[i - 1].parts >= 30)
    {
        cout << "Can't hold more than 30 Parts.";
    }

    // else it adds the parts
    else
    {

        inventoryList[i - 1].parts = inventoryList[i - 1].parts + addPart;

    }
    return;
}

// call to remove parts from the bin
void removeParts(struct InventoryInfo inventoryList [10], int i)
{

    // initialize parts variable and array
    int subPart;

    // asks user how many parts to remove
    cout << "How many parts are to be removed from the bin?: ";
    cin >> subPart;

    // validation rule for negative number
    if(subPart <= - 1)
    {
        cout << "Can't subtract Negative Parts." << endl;
    }

    // checks for negative number
    if(inventoryList[i - 1].parts - subPart < 0)
    {
        cout << "Can't have negative Parts." << endl;
    }
    
    // else it does the math and saves parts number
    else
    {

        inventoryList[i - 1].parts = inventoryList[i - 1].parts - subPart;

    }
    return;
}

// a submenu so there doesn't need to be 10 versions for each instance
void subMenu(struct InventoryInfo inventoryList [10], int i)
{
    // initialize choice to 0
    int choice = 0;

    // ask user what they want to do
    cout << "Please enter 1 to add parts" << endl;
    cout << "Please enter 2 to remove parts" << endl;
    cout << "Please enter 3 to exit" << endl;

    // start loop
    while (choice != 3)
    {
        // get choice
        cin >> choice;

        // if they want to add parts call function to add
        if (choice == 1)
        {
                
            addParts(inventoryList, i);
            choice = 3;

        }
            
        // if they want to remove parts call function to remove
        if (choice == 2)
        {
                
            removeParts(inventoryList, i);
            choice = 3;

        }
            
        // if they want to exit give them an exit statement
        if (choice == 3)
        {
                
            cout << "Exiting..." << endl;

        }
            
        // input validation
        else
        {
                
            cout << "Invalid Input, Please Try Again..." << endl;

        }
    }
    return;                             
}

// main function
int main()
{
    // array to store info for inventory
    struct InventoryInfo inventoryList [10];
    
    // initialize bin to their preassigned variables
    inventoryList[0].bin = "Valve";
    inventoryList[1].bin = "Bearing";
    inventoryList[2].bin = "Bushing";
    inventoryList[3].bin = "Coupling";
    inventoryList[4].bin = "Flange";
    inventoryList[5].bin = "Gear";
    inventoryList[6].bin = "Gear Housing";
    inventoryList[7].bin = "Vacuum Gripper";
    inventoryList[8].bin = "Cable";
    inventoryList[9].bin = "Rod";
    
    // initialize parts to their preassigned variables
    inventoryList[0].parts = 10;
    inventoryList[1].parts = 5;
    inventoryList[2].parts = 15;
    inventoryList[3].parts = 21;
    inventoryList[4].parts = 7;
    inventoryList[5].parts = 5;
    inventoryList[6].parts = 5;
    inventoryList[7].parts = 25;
    inventoryList[8].parts = 18;
    inventoryList[9].parts = 12;

    // initialize menu and submenu to 0
    int menuChoice = 0,
        subMenuChoice = 0,
        choice = 0;
    
    // menu loop
    while (menuChoice != 2)
    {
        
        // header display
        cout << "-----------------------------" << endl;
        cout << "  Part        Number of Parts" << endl;
        cout << "Description     In the bin" << endl;
        cout << "-----------------------------"<< endl;

        // print the info of each initialized variable in order
        for(int i = 0; i < 10; i++)
        {

            cout << "Bin " << (i + 1) << ": ";
            cout << inventoryList[i].bin << "     ";
            cout << inventoryList[i].parts << endl;

        }
        
        // out a simple menu for users to read
        cout << "Enter 1 to select a bin" << endl;
        cout << "Enter 2 to Exit" << endl;
        // get the users input for menu selection
        cin >> menuChoice;

        // call the menu choice to select bin
        if (menuChoice == 1)
        {
            
            // give them the choice of which bin to pick or exit
            cout << "Please enter the bin number, 1 - 10, you would like to select." << endl;
            cout << "Alternatively, enter 0 to exit: ";
            cin >> subMenuChoice;
            
            while (subMenuChoice != 0)
            {
                if (subMenuChoice >= 1 && subMenuChoice <= 10)
                {
                    
                    subMenu(inventoryList, subMenuChoice);
                    menuChoice = 0;
                    subMenuChoice = 0;

                }
                // if asking to exit, exit
                if (subMenuChoice == 0)
                {
                
                }

                // in case of error
                else
                {
                    
                    cout << "Incorrect Input, Please try again" << endl;
                    break;
                
                }
            }
        }
        // if wants to exit
        if (menuChoice == 2)
        {
            
            cout << "Exiting Application..." << endl;
        
        }

        // in case of error restart loop
        else
        {
        }
    }
}