#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    deque<int> dq;
    int N;
    cin >> N;

    while (N--) {
        string order;
        cin >> order;
        if (order == "push_front") { // 정수 X를 덱의 앞에 넣는다.
            int X;
            cin >> X;
            dq.push_front(X);
        } else if (order == "push_back") { // 정수 X를 덱의 뒤에 넣는다.
            int X;
            cin >> X;
            dq.push_back(X);
        } else if (order == "pop_front") { // 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력
            if ( !dq.empty() ) {
                cout << dq.front() << "\n";
                dq.pop_front();
            } else { // 만약 덱에 들어있는 정수가 없는 경우에는 -1 출력
                cout << -1 << "\n";
            }
        } else if (order == "pop_back") { // 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력
            if ( !dq.empty() ) {
                cout << dq.back() << "\n";
                dq.pop_back();
            } else { // 만약 덱에 들어있는 정수가 없는 경우에는 -1 출력
                cout << -1 << "\n";
            }
        } else if (order == "size") { // 덱에 들어 있는 정수의 개수를 출력
            cout << dq.size() << "\n";
        } else if (order == "empty") { // 덱이 비어있으면 1, 아니면 0을 출력
            cout << dq.empty() << "\n";
        } else if (order == "front") { // 덱의 가장 앞에 있는 수를 출력
            if ( !dq.empty() ) {
                cout << dq.front() << "\n";
            } else { // 만약 덱에 들어있는 정수가 없는 경우에는 -1 출력
                cout << -1 << "\n";
            }
        } else if (order == "back") { // 덱의 가장 뒤에 있는 수를 출력
            if ( !dq.empty() ) {
                cout << dq.back() << "\n";
            } else { // 만약 덱에 들어있는 정수가 없는 경우에는 -1 출력
                cout << -1 << "\n";
            }
        }
    }
}