import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int time []; // 건물 건설 시간
    static ArrayList<Integer>[] list; // 위상 정렬 간선 정보
    static int[] indegree; // 건설 사전 정보( indegree[i] : i번 건물을 짓기 위한 사전 건물의 갯수 )
    static int[] dp; // 각 번호의 건물을 짓는데 걸리는 비용의 최댓값
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        for (int t=0; t<testCase; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken()); // 건물 개수
            int K = Integer.parseInt(st.nextToken()); // 건물 건설 규칙 개수
            time = new int [N+1];
            dp = new int[N+1];
            indegree = new int[N+1];
            list = new ArrayList[N+1];

            st = new StringTokenizer(br.readLine());
            for (int i=1; i<=N; i++ ){ // i번 건물을 짓는데 걸리는 시간
                time[i] = Integer.parseInt(st.nextToken());
                list[i] = new ArrayList<>();
            }

            for (int i=0; i<K; i++) { // X 이후에 Y 건물 짓기 가능
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                list[X].add(Y);
                indegree[Y]++;
            }

            int W = Integer.parseInt(br.readLine()); // 지으면 끝
            dp = new int[N+1];
            find();
            System.out.println(dp[W]);

        }
    }

    // bfs 방식?
    public static void find() {
        Queue<Integer> queue = new LinkedList<>();

        for (int i=1; i<indegree.length; i++) {
            if ( indegree[i] == 0 ) { // 사전 건설 건물 X
                dp[i] = time[i];
                queue.add(i);
            }
        }

        while ( !queue.isEmpty() ) {
            int q = queue.poll();

            for (int i=0; i<list[q].size(); i++) {
                int next = list[q].get(i);
                dp[next] = Math.max(dp[next], dp[q] + time[next]); // 다음 건물을 짓는 시간까지 계산
                indegree[next]--;
                if (indegree[next] == 0) { // 다음 건물에 더 지어야 할 사전 건물이 없다면
                    queue.add(next); // 다음 큐에 추가해서 지어주도록 함
                }
            }
        }
    }
}

// W를 짓기 위한 건물 순서 찾고
// 그 순서대로 짓기 위한 시간을 찾기
// 동시에 여러 개의 건물을 지을 수도 있음
