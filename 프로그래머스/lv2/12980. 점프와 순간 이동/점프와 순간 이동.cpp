#include <iostream>
using namespace std;

int solution(int n)
{
    int ans = 0;
    
    // 한 번에 K칸을 앞으로 점프하거나, (현재까지 온 거리) * 2의 위치로 순간이동 가능
    // 점프하면 K만큼 건전지 사용량이 든다.
    // 건전지 사용량을 최소로 N만큼 이동하기
    
    while (n > 0) {
        if ( n % 2 == 0 ) n /= 2; // 짝수면 나누고
        else { // 홀수면 한칸 이동
            n -= 1;
            ans += 1;
        }
    }
    return ans;
}