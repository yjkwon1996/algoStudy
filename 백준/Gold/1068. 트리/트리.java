import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, erase;
    static int parent[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        parent = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            parent[i] = Integer.parseInt(st.nextToken());
        }

        erase = Integer.parseInt(br.readLine());

        // 부모가 erase인 노드를 삭제 -> 그 삭제된 노드의 자식도 모두 다 삭제
        for (int i=0; i<N; i++) {
            if(parent[i] == erase) {
                dfs(i);
            }
        }
        parent[erase] = -2;

        // 지워진 곳은 -2
        // 리프 노드만 찾으면 끝 -> 자식이 없는 노드
        int leaf = 0;
        for (int i=0; i<N; i++) {
            if (findChild(i) ) {
                leaf++;
            }
        }
        System.out.println(leaf);

    }

    static void dfs(int idx) {
        for(int i=0; i<N; i++) {
            if (parent[i] == idx) {
                dfs(i);
            }
        }
        parent[idx] = -2;
    }

    static boolean findChild(int idx) {
        if (parent[idx] == -2) { // 삭제된 노드면 끝
            return false;
        }
        for (int i=0; i<N; i++) {
            if (parent[i] == idx) {
                return false;
            }
        }
        return true;
    }

}
