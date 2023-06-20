#include <iostream>

using namespace std;

int solution(int n, int a, int b)
{
    int answer = 0;
    // n명 참가, a번이 b번과 몇 번째 라운드에서 만나는지
    
    while (a != b) { // 만날 때까지 반복해서
        answer += 1; // 라운드 수 증가
        a = (a + 1) / 2; // 홀수든 짝수든 (x+1) / 2 하면 다음 라운드 번호가 나옴
        b = (b + 1) / 2;
    }
    // cout << answer << endl;

    return answer;
}