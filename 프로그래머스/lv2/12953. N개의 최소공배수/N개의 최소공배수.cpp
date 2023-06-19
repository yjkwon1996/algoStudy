#include <string>
#include <vector>

using namespace std;

int gcd(int x, int y) { // 최대공약수. 
    return x % y == 0 ? y : gcd(y, x % y);
}

int lcm(int x, int y) { // 최소공배수
    return x * y / gcd(x, y);  
}

// 유클리드 호제법
// G(A, B) = G(B, A%B)와 같다를 이용

int solution(vector<int> arr) {
    int answer = arr[0];
    
    for (int i=1; i<arr.size(); i++) {
        answer = lcm(answer, arr[i]); // 최소공배수 찾기
    }
    
    return answer;
}