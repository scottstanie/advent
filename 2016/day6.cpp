#include <stdlib.h>
#include <unordered_map>
#include <fstream>
#include <iostream>
#include <string>

typedef std::unordered_map<std::string,int> MYMAP;
int main() {

    std::ifstream infile("day6_input.txt");
    char a, b, c, d, e, f, g, h;
    MYMAP m1;
    std::unordered_map <std::string, int> m2;
    std::unordered_map <std::string, int> m3;
    std::unordered_map <std::string, int> m4;
    std::unordered_map <std::string, int> m5;
    std::unordered_map <std::string, int> m6;
    std::unordered_map <std::string, int> m7;
    std::unordered_map <std::string, int> m8;
    while (infile >> a >> b >> c >> d >> e >> f >> g >> h) {
        // std::cout << a << std::endl;
        if (m1[a]) {
            m1[a]++;
        } else {
            m1[a] = 1;
        }
//        m1[a]++;
//        m2[b]++;
//        m3[c]++;
//        m4[d]++;
//        m5[e]++;
//        m6[f]++;
//        m7[g]++;
//        m8[h]++;        
    }
    std::cout << m1["a"] << std::endl;
    return 0;
}
