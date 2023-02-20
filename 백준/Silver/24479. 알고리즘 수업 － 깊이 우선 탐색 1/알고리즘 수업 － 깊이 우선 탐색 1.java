import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] nodes;
    static boolean [] visited;
    static int [] ans;
    static int now = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        nodes = new ArrayList[N+1];
        visited = new boolean[N+1];
        ans = new int[N+1];

        for (int i = 1; i <= N; i++) {
            nodes[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            nodes[u].add(v);
            nodes[v].add(u);
        }

        for (int i=1; i<=N; i++) {
            Collections.sort(nodes[i]);
        }

        visited[R] = true;
        dfs(R);

        for (int i=1; i<=N; i++) {
            System.out.println(ans[i]);
        }
    }

    static void dfs(int cnt) {
        ans[cnt] = ++now;
        for (int nt : nodes[cnt]) {
            if (visited[nt]) continue;
            visited[nt] = true;
            dfs(nt);
        }
    }
}
