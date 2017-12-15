#include <stdio.h>
#include <stdbool.h>


long next_num(long unsigned cur_num, int factor, long modulus) {
  long long t = cur_num * factor;
  return t % modulus;
}


bool matching(long unsigned a, long unsigned b) {
  long unsigned p = 1<<16;
  if (a < b) {
    return ((b - a) % p) == 0;
  } else {
    return ((a - b) % p) == 0;
  }

}

int main() {
  int fa = 16807;
  int fb = 48271;
  long long m = 2147483647;

  long long sa = 679;
  long long sb = 771;

  // sa = 65;
  // sb = 8921;

  // printf("%d\n", matching(25556042, 1431495498));

  int match_count = 0;

  long judge_count = 5000000;
  long j_iter= 0;

  while (j_iter < judge_count) {
  // for (int i=0; i<40000000; ++i) {


    sa = next_num(sa, fa, m);
    sb = next_num(sb, fb, m);
    while (sa % 4 > 0) {
      sa = next_num(sa, fa, m);
    }
    while (sb % 8 > 0) {
      sb = next_num(sb, fb, m);
    }

    ++j_iter;
    if (matching(sa, sb)) {
      ++match_count;
      // printf("%li\n", j_iter);
      // break;
    }
  }
  printf("%d\n", match_count);

  return 0;
}

