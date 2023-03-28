#include <iostream>
#include <list>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string str;
    cin >> str;
    
    list<char> lst;
    for (auto c : str) {
        lst.push_back(c);
    }

    auto cursor = lst.end();

    int M; // 명령의 갯수
    cin >> M;

    while (M--) {
        char op; // 명령어
        cin >> op;

        if (op == 'L') { // 커서를 왼쪽
            if (cursor != lst.begin() ) cursor--;
        } else if (op == 'D') { // 커서를 오른쪽
            if (cursor != lst.end() ) cursor++;
        } else if (op == 'B') { // 커서 왼쪽 문자 삭제
            if (cursor != lst.begin() ) {
                cursor--;
                cursor = lst.erase(cursor);
            }
        } else if (op == 'P') { // 커서 왼쪽에 문자 추가
            char add;
            cin >> add;
            lst.insert(cursor, add);
        }
    }

    for (auto c : lst) {
        cout << c;
    }

}