#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

int part1() {
  int line;
  int sum = 0;

  while (cin >> line) {
    sum += line;
  }
  return sum;
}

int part2() {
  vector<int> all_ints;
  set<int> reached_values;
  long line, sum = 0;
  while (cin >> line) {
    all_ints.push_back(line);
    sum += line;
    if (reached_values.find(sum) != reached_values.end()) {
      return sum;
    } else {
      reached_values.insert(sum);
    }
  }
  bool found = false;

  while (!found) {
    for (auto n : all_ints) {
      // cout << sum << endl;
      sum += n;
      if (reached_values.find(sum) != reached_values.end()) {
        return sum;
      } else {
        reached_values.insert(sum);
      }
    }
  }
  return sum;
}

int main() {
  // int p1 = part1();
  // cout << p1 << endl;

  int p2 = part2();
  cout << p2 << endl;
}
