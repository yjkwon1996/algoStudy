// D-Day. https://www.acmicpc.net/problem/1308
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 매 달 일 수 
int monthDay[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

// 윤년 확인용
int leapYear(int year) {
	if (year % 400 == 0) return 1;
	if (year % 100 == 0) return 0;
	if (year % 4 == 0) return 1;

	return 0;
}

// 년/월/일 -> 일
int toDay(int year, int month, int day) {
	int total = 0;

	for (int i = 1; i < year; i++) {
		total += (leapYear(i) ? 366 : 365); // 윤년이면 366, 아니면 365
	}

	for (int i = 1; i < month; i++) {
		if (i == 2 && leapYear(year)) {
			total += 29;
		}
		else {
			total += monthDay[i - 1];
		}
	}
	total += day;
	return total;
}

int main() {
	int nowYear, nowMonth, nowDay;
	int targetYear, targetMonth, targetDay;
	
	scanf("%d %d %d", &nowYear, &nowMonth, &nowDay);
	scanf("%d %d %d", &targetYear, &targetMonth, &targetDay);

	// 천년 이상
	if (targetYear > nowYear + 1000 || (targetYear == nowYear + 1000 && (targetMonth > nowMonth || (targetMonth == nowMonth && targetDay >= nowDay)))) {
		printf("gg");
		return 0;
	}

	// 일수로 변환
	int now = toDay(nowYear, nowMonth, nowDay);
	int target = toDay(targetYear, targetMonth, targetDay);

	int answer = target - now;
	printf("D-%d", answer);

	return 0;
}
