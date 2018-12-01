#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using std::cin;
using std::string;
using std::cout;
using std::endl;

int main() {
  string line;
  int n;
  int checksum = 0;
  while(std::getline(cin, line)){
    std::stringstream linestream(line);
    int maxn = 0, minn = 1000000;
    while (linestream >> n) {
      if (n > maxn) maxn = n;
      if (n < minn) minn = n;
  }
  checksum += (maxn - minn);

  }
  cout << checksum << endl;
  return 0;
}
