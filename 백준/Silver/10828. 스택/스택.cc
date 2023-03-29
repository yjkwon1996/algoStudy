#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    stack<int> S;

    while (N--) {
        string order;
        cin >> order;

        if ( order == "push" ) { // 정수 X를 스택에 넣는 연산
            int X;
            cin >> X;
            S.push(X);
        } else if ( order == "pop" ) { // 스택에서 가장 위에 있는 정수를 뺴고 출력
            if ( !S.empty() ) {
                cout << S.top() << "\n";
                S.pop();
            } else { // 스택에 들어있는 정수가 없는 경우에는 -1 출력
                cout << -1 << "\n";
            }
        } else if ( order == "size" ) { // 스택에 들어있는 정수의 개수를 출력
            cout << S.size() << "\n";
        } else if ( order == "empty" ) { // 스택이 비어있으면 1, 아니면 0을 출력
            cout << (int)S.empty() << "\n";
        } else if ( order == "top" ) { // 스택의 가장 위에 있는 정수를 출력
            if ( !S.empty() ) {
                cout << S.top() << "\n";
            } else { // 스택에 들어있는 정수가 없는 경우에는 -1 출력
                cout << -1 << "\n";
            }
        }
    }

}