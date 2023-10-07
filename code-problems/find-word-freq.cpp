/**
 * Print frequencies of individual words in a string
 * 
 * demonstrate use of stringstream and map
 * https://www.geeksforgeeks.org/stringstream-c-applications/
 *
 * 
 * Input : Geeks For Geeks Quiz Geeks Quiz Practice Practice
Output : For -> 1
         Geeks -> 3
         Practice -> 2
         Quiz -> 2

Input : Word String Frequency String
Output : Frequency -> 1
         String -> 2
         Word -> 1 
 **/

// CPP program to demonstrate use of stringstream
// to count frequencies of words.
#include <bits/stdc++.h>
using namespace std;

void printFrequency(string st)
{
    // each word it mapped to it's frequency
    map<string, int> FW;
    stringstream ss(st); // Used for breaking words
    string Word;         // To store individual words

    while (ss >> Word)
        FW[Word]++;

    map<string, int>::iterator m;
    for (m = FW.begin(); m != FW.end(); m++)
        cout << m->first << " -> "
             << m->second << "\n";
}

// Driver code
int main()
{
    string s = "Geeks For Geeks Ide";
    printFrequency(s);
    return 0;
}
