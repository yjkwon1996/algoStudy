#include <string>
#include <vector>
#include <iostream>

using namespace std;

long long solution(int n) {
    long long answer = 0;
    
    // 한번이 1칸 또는 2칸 뛰기 가능. 칸의 수가 n일 때 끝에 도달하는 방법이 몇 가지인지
    // 1234567을 나눈 나머지를 리턴
    // 피보나치 수열? dp?
    
    long long arr[n+1];
    arr[0] = 1;
    arr[1] = 1;
    for (int i=2; i<=n; i++) {
        arr[i] = (arr[i-1] + arr[i-2]) % 1234567;
        // cout << arr[i] << endl;
    }
    
    answer = arr[n];
    
    return answer;
}