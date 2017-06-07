#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct box {
    int len;
    int width;
    int height;
} box;


int volume(box *b) {
    return b->len * b->width * b->height;
}


int find_index_max_side(int sides[3]) {
    int max_size_index = 0;  // start with first
    for (int i = 1; i < 3; ++i) {
        if (sides[i] > sides[max_size_index])
            max_size_index = i;
    }
    return max_size_index;
}

int smallest_side_perimeter(box *b) {
    int sides[3] = { b->len, b->width, b->height };
    int max_size_index = find_index_max_side(sides);
    int side1 = (max_size_index + 1) % 3;
    int side2 = (max_size_index + 2) % 3;

    return 2 * sides[side1] + 2 * sides[side2];
}

int total_ribbon(box *b) {
    return volume(b) + smallest_side_perimeter(b);
}

void arr_to_box(int sides[3], box *b) {
    b->len = sides[0];
    b->width = sides[1];
    b->height = sides[2];
}

int main() {
    /* Tests */
    box b1 = { 4, 2, 3 };
    printf("%d\n", total_ribbon(&b1));
    box b2 = { 1, 1, 10 };
    printf("%d\n", total_ribbon(&b2));
    box b3 = { 20, 3, 11 };
    printf("%d\n", total_ribbon(&b3));

    int tp = 0;

    FILE *fp = fopen("input.txt", "rb");
    char *line = NULL;
    size_t len = 0;
    char *token_end;
    char *delim = "x";
    while (getline(&line, &len, fp) != -1) {
        // printf("%s", line);
        int sides[3];

        char *token = strtok(line, delim);
        for (int i = 0; i < 3; ++i, token=strtok(NULL, delim)) {
            sides[i] = strtol(token, &token_end, 10);
        }

        box b;
        arr_to_box(sides, &b);
        tp += total_ribbon(&b);

    }
    printf("Total: %d\n", tp);

    return 0;
}
