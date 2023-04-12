#include <iostream>

using namespace std;
long long A, B, C, value;

long long pow(long long B) {
    if (B == 0) return 1;
    if (B == 1) return A % C;
    value = pow(B / 2) % C;
    if (B % 2 == 0) return value * value % C;
    return value * value % C * A % C;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> A >> B >> C;
    cout << pow(B);
    return 0;
}
