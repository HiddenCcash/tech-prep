/**
 * Given a long int which denotes seconds, output a string in the format of
 * HH:MM:SS
 **/

#include <iostream>
#include <stdio.h>

using namespace std;
using std::stof;

int main()
{
    std::string str = "4000";
    long uptime = stof(str);

    // int uptime = 4000;

    // option 1
    int hours = uptime / 3600;
    int remaining_seconds = uptime - (hours * 3600);
    int mins = remaining_seconds / 60;
    int secs = uptime - (hours * 3600 + mins * 60);

    // output
    cout << hours << endl;
    cout << mins << endl;
    cout << secs << endl;

    char output[50];
    sprintf(output, "%02u:%02u:%02u", hours, mins, secs);

    cout << output << endl;

    return 0;
}