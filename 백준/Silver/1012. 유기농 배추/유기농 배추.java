import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int [][] arr;
    static boolean [][] visited;
    static int [] dx = {0, 0, -1, 1}; // 상하좌우
    static int [] dy = {-1, 1, 0, 0};
    static int ans, M, N;
    static Queue<Node> queue = new LinkedList<Node>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int t=0; t<testCase; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken()); // 밭의 가로길이
            N = Integer.parseInt(st.nextToken()); // 밭의 세로길이
            arr = new int [N][M];
            visited = new boolean[N][M];
            ans = 0;
            int K = Integer.parseInt(st.nextToken()); // 배추가 심어져 있는 위치의 개수

            for (int i=0; i<K; i++) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                arr[Y][X] = 1;
            }

            for (int i=0; i<N; i++) {
                for (int j=0; j<M; j++) {
                    if (arr[i][j] == 1 && !visited[i][j]) { // 지렁이가 아직 가지 않은 곳이면(못가는곳)
//                        dfs(j, i);
                        bfs(j, i);
                        ans++; // 지렁이를 한마리 추가
                    }
                }
            }
            System.out.println(ans);
        }

    }
    static void dfs(int x, int y) {
        visited[y][x] = true;

        for (int d=0; d<4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];

            // 사방 탐색, 배추가 있고 지렁이가 갈 수 있는 곳
            if (ny>=0 && ny<N && nx>=0 && nx<M && !visited[ny][nx] && arr[ny][nx] == 1 ) {
                dfs(nx, ny);
            }
        }
    }

    static void bfs(int x, int y) {
        queue.add(new Node(x, y));
        visited[y][x] = true;

        while ( !queue.isEmpty() ) {
            Node node = queue.poll();

            for (int d=0; d<4; d++) {
                int ny = node.y + dy[d];
                int nx = node.x + dx[d];

                // 사방 탐색, 배추가 있고 지렁이가 갈 수 있는 곳
                if (ny >= 0 && ny < N && nx >= 0 && nx < M && !visited[ny][nx] && arr[ny][nx] == 1) {
                    visited[ny][nx] = true;
                    queue.add(new Node(nx, ny));
                }
            }
        }

    }
    static class Node {
        int x;
        int y;
        public Node (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}

// 지렁이는 인접한 배추가 있는 곳으로 이동 가능
// 모든 배추가 있는 곳에 지렁이를 두려면 최소 몇마리가 필요?
// BFS or DFS