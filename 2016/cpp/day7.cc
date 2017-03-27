#include <iostream>
#include <vector>
#include <string>

using std::string;
using std::vector;
using std::cout;
using std::cin;
using std::endl;

bool isAbba(string fourChars)
{
    if (fourChars.length() < 4)
        return false;

    return (fourChars[0] == fourChars[3] && 
            fourChars[0] != fourChars[1] && 
            fourChars[1] == fourChars[2]);
}


bool supportsTls(string fullString)
{
    string chunk;
    bool inBracket = false;
    bool found = false;

    for (size_t i = 0; i < fullString.length() - 3; ++i)
    {
        if (fullString[i] == '[')
        {
            inBracket = true;
            continue;
        } else if (fullString[i] == ']')
        {
            inBracket = false;
            continue;
        }
        chunk = fullString.substr(i, 4);

        if (isAbba(chunk))
        {
            if (inBracket) 
                return false;
            found = true;
        }
    }
    return found;
}

int main()
{

    string test1 = "abba[mnop]qrst";
    string test2 = "abcd[bddb]xyyx";
    string test3 = "aaaa[qwer]tyui";
    string test4 = "ioxxoj[asdfgh]zxcvbn";
    // cout << supportsTls(test1) << endl;
    // cout << supportsTls(test2) << endl;
    // cout << supportsTls(test3) << endl;
    // cout << supportsTls(test4) << endl;
    // cout << endl << endl;

    int numSupported = 0;
    string line;
    while (getline(cin, line))
    {
        if (supportsTls(line))
            ++numSupported;
    }
    cout << numSupported << " supported!" << endl;

    return 0;
}
