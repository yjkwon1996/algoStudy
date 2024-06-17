// 수열의 변화 https://www.acmicpc.net/problem/1551 
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int N, K;
	scanf("%d %d", &N, &K);
	int list[30] = { 0 };
	char buffer = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", &list[i]);
		scanf("%c", &buffer);
	}

	int point = N;
	while (K > 0) {
		for (int i = 0; i < point - 1; i++) {
			list[i] = list[i + 1] - list[i];
		}
		K--;
		point--;
	}
	for (int i = 0; i < point; i++) {
		printf("%d", list[i]);
		if (i < point - 1) {
			printf(",");
		}
	}


	return 0;
}