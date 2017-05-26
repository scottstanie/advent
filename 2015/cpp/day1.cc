#include <iostream>
#include <vector>
#include <string>

using std::string;
using std::cout;
using std::cin;
using std::endl;

int main(int argc, char *argv[])
{
    string input;
    getline(cin, input);
    int curFloor = 0;
    for (auto c: input)
    {
        if(c == '(') ++curFloor;
        else if(c == ')') --curFloor;
    }
    cout << "Final floor: " << curFloor << endl;

    // Part 2:
    curFloor = 0;
    int position = 1;
    for (auto c: input)
    {
        if(c == '(') ++curFloor;
        else if(c == ')') --curFloor;

        if (curFloor < 0) break;
        ++position;

    }
    cout << "First basement floor: " << position << endl;
    return 0;
}
