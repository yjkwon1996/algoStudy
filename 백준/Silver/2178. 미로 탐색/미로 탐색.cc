#include <iostream>
#include <queue>

#define x first
#define y second

using namespace std;
int dy[4] = {-1, 1, 0 ,0}; // 상하좌우
int dx[4] = {0, 0, -1, 1};
int N, M;
int arr[102][102];
string input[102];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;

    for (int i=0; i<N; i++) {
        cin >> input[i];
        fill(arr[i], arr[i]+M, -1); // -1로 초기화
    }
    queue<pair<int, int>> q;
    q.push({0, 0});
    arr[0][0] = 0;

    while (!q.empty()) {
        auto now = q.front();
        q.pop();

        for (int d=0; d<4; d++) {
            int nx = now.x + dx[d];
            int ny = now.y + dy[d];
            if (nx>=0 && nx<N && ny>=0 && ny<M && arr[nx][ny]<0 && input[nx][ny] == '1') {
                arr[nx][ny] = arr[now.x][now.y]+1;
                q.push({nx, ny});
            }
        }
    }
    cout << arr[N-1][M-1]+1;
}