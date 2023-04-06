#include <iostream>
#include <queue>
using namespace std;

int dx[4] = {0, 0, -1, 1}; // 상하좌우
int dy[4] = {-1, 1, 0, 0};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    int arr[502][502];
    bool visited[502][502];
    cin >> n >> m;

    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> arr[i][j];
        }
    }

    int mx = 0; // 가장 넓은 그림
    int cnt = 0; // 그림의 개수

    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (arr[i][j] == 0 || visited[i][j]) continue; // 색칠이 안됐거나 이미 확인했으면 스킵

            // 새 그림 발견. 큐에 넣고 bfs
            cnt++;
            queue<pair<int, int>> que; // 각 좌표를 큐에 저장
            visited[i][j] = true;
            que.push({i, j});
            int area = 0;

            while(!que.empty()) { // 큐가 빌 때까지
                area++;
                pair<int, int> now = que.front(); // 큐를 꺼내서 큐와 연결된 다른 색칠된 그림이 있는지 확인
                que.pop();

                for (int d=0; d<4; d++) {
                    int nx = now.first + dx[d];
                    int ny = now.second + dy[d];

                    // 범위 안에서 색칠되어있고 아직 확인하지 않았다면 큐에 추가
                    if (nx>=0 && nx<n && ny>=0 && ny<m && !visited[nx][ny] && arr[nx][ny] == 1) {
                        visited[nx][ny] = true;
                        que.push({nx, ny});
                    } 
                }
            }
            // 큐를 돌고 나서 그림의 크기를 확인
            mx = max(mx, area);
        }
    }
    cout << cnt << "\n" << mx;
}