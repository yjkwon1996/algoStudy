#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<int> q;
    int N;
    cin >> N;
    while(N--) {
        string order;
        cin >> order;

        if (order == "push") { // 정수 X를 큐에 넣는 연산
            int X;
            cin >> X;
            q.push(X);
        } else if (order == "pop") { // 큐에서 가장 앞에 있는 정수를 빼고, 수를 출력한다.
            if ( !q.empty() ) {
                cout << q.front() << "\n";
                q.pop();
            } else { // 큐에 들어있는 정수가 없으면 -1 출력
                cout << -1 << "\n";
            }
        } else if (order == "size") { // 큐에 들어있는 정수의 개수를 출력
            cout << q.size() << "\n";
        } else if (order == "empty") { // 큐가 비어있으면 1, 아니면 0을 출력
            cout << q.empty() << "\n";
        } else if (order == "front") { // 큐의 가장 앞에 있는 정수를 출력
            if ( !q.empty() ) {
                cout << q.front() << "\n";
            } else { // 큐에 들어있는 정수가 없으면 -1 출력
                cout << -1 << "\n";
            }
        } else if (order == "back") { // 큐의 가장 뒤에 있는 정수를 출력
            if ( !q.empty() ) {
                cout << q.back() << "\n";
            } else { // 큐에 들어있는 정수가 없으면 -1 출력
                cout << -1 << "\n";
            } 
        }
    }

}