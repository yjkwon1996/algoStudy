#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N; // 사람 수
vector<int> arr[51]; // 친구 관계를 나타내는 인접배열
bool visited[51]; // 방문 여부
int ans[51] = {0}; // i번째 사람의 2-친구 수

// 깊이 2까지 들어가는 dfs
void dfs(int depth, int idx) {
    visited[idx] = true; // 방문 체크
    if (depth == 2) return; // 깊이 2면 out
    for (int i=0; i<arr[idx].size(); i++) {
        dfs(depth+1, arr[idx][i]);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    char c;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> c;
            if(c == 'Y') arr[i].push_back(j); // 친구면 넣어주기
        }
    }

    for (int i=0; i<N; i++) {
        int cnt = 0;
        for (int j=0; j<51; j++) {
            visited[j] = false;
        }

        dfs(0, i);

        for(int j=0; j<N; j++) {
            if(visited[j]) {
                cnt++;
            }
        }

        // 2-친구 수일 때
        ans[i] = cnt-1; // 자기 자신 빼기
    }

    sort(ans, ans+51); // 가장 큰 수 찾아서 출력
    cout << ans[50];

    return 0;
}