#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (true) {
        string str;
        getline(cin, str); // 공백을 포함한 입력
        if ( str == ".") break; // 입력 종료 
        stack<char> s;

        bool flag = true; // 마지막까지 완성가능한지 확인용

        for (auto c : str) {
            if (c == '(' || c == '[') { // 여는 괄호를 발견하면 스택에 넣고
                s.push(c);
            } else if (c == ')') { // 닫는 괄호를 발견했다면 앞에 나온 괄호와 맞는지 확인
                if (!s.empty() && s.top() == '(') { // 맞으면 스택에서 하나 제거 & 스택이 비어있는지 검사하지 않으면 에러 발생함 - s.top()에서 발생함!!!!!!!!!!!!!!!
                    s.pop();
                } else { // 아니면 반복 종료
                    flag = false;
                    break;
                }
            } else if (c == ']') { // 닫는 괄호를 발견했다면 앞에 나온 괄호와 맞는지 확인
                if (!s.empty() && s.top() == '[') { // 맞으면 스택에서 하나 제거 & 스택이 비어있는지 검사하지 않으면 에러 발생함
                    s.pop();
                } else { // 아니면 반복 종료
                    flag = false;
                    break;
                }
            }
        }

        if ( !s.empty() || !flag ) { // 다 탐색했는데 괄호가 남거나 짝이 맞지 않다면
            cout << "no" << "\n";
        } else {
            cout << "yes" << "\n";
        }


    }
}