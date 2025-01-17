#include <stdio.h>

#define ROWS 8
#define COLS 4

static inline int modulus(int a, int b)
{
	return a < 0 ? b + (a % b) : a % b;
}

int main()
{
	int half_block[ROWS][COLS];
	for (int i = 0; i < ROWS; ++i) {
		for (int j = 0; j < COLS; ++j)
			half_block[i][j] = i * COLS + j;
	}
	int expanded_block[ROWS][COLS+2];
	for (int i = 0; i < ROWS; ++i) {
		expanded_block[i][0] = half_block[(i - 1) % (ROWS * COLS)][COLS - 1];
		for (int j = 0; j < COLS; ++j)
			expanded_block[i][j + 1] = half_block[i][j];
		expanded_block[i][COLS + 1] = half_block[(i + 1) % (ROWS * COLS)][0];
	}
	for (int i = 0; i < ROWS; ++i) {
		for (int j = 0; j < COLS + 2; ++j)
			printf("%d ", expanded_block[i][j]);
		putchar('\n');
	}
	return 0;
}
