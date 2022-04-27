// Description: Write a program that opens a file, reads records into a container of data structures,
// and prints out the sum in order.
//
// Course Name : C++ programming 2541
// course num: 272290
// Author: Connor Delgado
// Version: 1.2
// Date: 04/16/22

#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include "cost.h"               // custom struct file cost.h

using namespace std;

// the functions to be used
vector<Cost> parseAccount(ifstream *spot, vector<Cost> data);
double sumAccounts(vector<Cost> data);

// the main function
int main()
{
    // initialize vector data
    vector <Cost> data;

    // open the file
    ifstream inFile;
    inFile.open("costfile.txt", ios::in);

    // get the first line as it's a header and doesn't match data types
    std::string line1;

    std::getline(inFile, line1);

    // data vector = parse account, pass part of file we're stream at and vector  
    data = parseAccount(&inFile, data);
    
    // close file
    inFile.close();

    // initialize variable sum for amount total
    double sum = 0.00;
    
    // get the sum and display it
    sum = sumAccounts(data);
    cout << "The sum of the accounts is " << sum << endl;

    // as requested we now output the file as a binary file
    // open the binary and prep for binary
    ofstream binaryFile;
    binaryFile.open("outfile.txt", ios::out | ios::binary);

    // write line 1 to binary, taken out earlier
    binaryFile.write((char*)&line1, sizeof(line1));

    // loop to write the other lines from the vector to binary
    for(int i = 0; i < data.size(); i++)
    {
        
        binaryFile.write((char*)&data[i], sizeof(data[i]));

    }
    // close the binary file
    binaryFile.close();
}

// parse Account function type Cost, this allows push_back to work
vector<Cost> parseAccount(ifstream *spot, vector<Cost> data)
{
    // initialize variables
    std::string description;
    double amount;
    int itemNumber;

    // while loop that assigns variable skipping whitespace
    while(*spot >> description >> amount >> itemNumber)
    {
        // bring in variables from struct and assign to struct variables
        Cost tempCost;

        // assign each variable to cost variables
        tempCost.description = description;
        tempCost.amount = amount;
        tempCost.itemNumber = itemNumber;
        
        // push to vector
        data.push_back(tempCost);
    }
    
    // return vector data
    return data;
}

// double type function to get the sum of the accounts
double sumAccounts(vector<Cost> data)
{
    // initialize sum to 0
    double sum = 0.00;
    
    // for each value in the amount variable of the vector add to sum and repeat until out of amounts
    for (int i = 0; i < data.size(); i++)
    {
        sum = sum + data[i].amount;
    }
    
    // return the double
    return sum;
}