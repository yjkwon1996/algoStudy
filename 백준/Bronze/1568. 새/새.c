// 새. https://www.acmicpc.net/problem/1568
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	int N;
	int time = 0;
	scanf("%d", &N);

	while (N > 0) {
		int K = 1;
		while (K <= N) {
			N -= K;
			K++;
			time++;
		}
	}
	printf("%d", time);
	return 0;
}