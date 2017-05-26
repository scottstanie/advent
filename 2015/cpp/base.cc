#include <iostream>
#include <vector>
#include <string>

using std::string;
using std::cout;
using std::cin;
using std::endl;


template <typename ElemType>
void printArray(vector<ElemType> vec)
{
        cout << "[ ";
        for (auto e: vec)
        {
            cout << e << " ";
        }
        cout << ']';
}

int main(int argc, char *argv[])
{
    return 0;
}
