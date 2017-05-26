#include <iostream>
#include <vector>
#include <string>
#include <regex>
#include <numeric>

using std::string;
using std::cout;
using std::cin;
using std::endl;

int surface(int l, int w, int h)
{
    std::vector<int> v;
    v.push_back(2 * l * w);
    v.push_back(2 * l * h);
    v.push_back(2 * w * h);
    int smallest = *std::min_element(v.begin(), v.end());
    v.push_back(smallest / 2);
    return std::accumulate(v.begin(), v.end(), 0);
}

int main()
{
    string line;
    // Tests:
    cout << surface(2, 3, 4) << endl;
    cout << surface(1, 1, 10) << endl;
    std::vector<int> surfaces;

    std::regex r("(\\d+)x(\\d+)x(\\d+)");
    std::smatch matchList;
    while(getline(cin, line))
    {

        std::regex_match(line, matchList, r);
        int l = std::stoi(matchList[1].str());
        int w = std::stoi(matchList[2].str());
        int h = std::stoi(matchList[3].str());
        surfaces.push_back(surface(l, w, h));
    }
    cout << "Total paper: " << std::accumulate(surfaces.begin(), surfaces.end(), 0) << endl;
    return 0;
}
