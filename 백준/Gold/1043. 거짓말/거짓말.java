import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int parent [];
    static boolean fact [];
    static ArrayList<Integer>[] people;
    static int N, M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        people = new ArrayList[M];
        for (int i=0; i<M; i++) {
            people[i] = new ArrayList<>();
        }
        parent = new int[N+1];
        for (int i=1; i<=N; i++) {
            parent[i] = i;
        }

        st = new StringTokenizer(br.readLine());
        int num = Integer.parseInt(st.nextToken()); // 진실을 아는 사람의 수
        fact = new boolean [N+1]; // fact[x] = true; -> x는 진실을 안다.
        for (int n=0; n<num; n++) { // 그 사람들의 번호
            fact[Integer.parseInt(st.nextToken())] = true;
        }

        // 파티와 참석하는 인원 정보를 받아오면서 부모 갱신
        int pre, next;
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            num = Integer.parseInt(st.nextToken()); // 각 파티마다 오는 사람의 수
            if ( num > 0) { // 한명 이상이 왔다면 첫 한명은 그냥 추가
                pre = Integer.parseInt(st.nextToken());
                people[i].add(pre);
                for (int n = 1; n < num; n++) { //
                    next = Integer.parseInt(st.nextToken());
                    people[i].add(next);
                }
            }
        }

        // union
        for (int i=0; i<M; i++ ) {
            if (people[i].size() >= 2) {
                for (int j=1; j<people[i].size(); j++) {
                    union(people[i].get(j-1), people[i].get(j));
                }
            }

        }


        // 진실을 아는 사람들과 같이 파티에 참여한 사람을 처리
        for (int i=1; i<fact.length; i++) {
            if (fact[i]) {
                fact[find(i)] = true;
            }
        }

        // 진실을 모르는 사람만 찾아서
        int parent;
        int ans = 0;
        for(int i=0; i<M; i++) {
            if(people[i].size() > 0) {
                parent = find(people[i].get(0));
                if ( !fact[parent] ) ans++;
            }
        }

        System.out.println(ans);
    }

    static int find(int idx) { // 부모를 찾아서 리턴
        if (parent[idx] == idx) {
            return idx;
        } else
        return find(parent[idx]);
    }
    static boolean union(int a, int b) {
        if (find(a) != find(b)) { // 두 노드의 부모 비교
            if ( find(a) > find(b) ) { // 통합
                for(int i=0; i<=N; i++) {
                    if (parent[i] == find(a)) {
                        parent[i] = find(b);
                    }
                }
            } else {
                for(int i=0; i<=N; i++) {
                    if (parent[i] == find(b)) {
                        parent[i] = find(a);
                    }
                }
            }
            return true;
        }
        return false; // 이미 같은 부모를 가지고 있음
    }
}

// 사람 수 N이 주어질 때
// 파티의 수는 M
// 진실을 아는 사람이 존재 - fact
// 각 파티마다 오는 사람들 - party
// 진실을 아는 사람이 있는 곳에서는 이야기 X
// 진실을 아는 사람과 같은 파티에 참여한 사람이 있는 곳에서도 이야기 X
// (1이 진실을 알 때 1과 2가 같이 참여했다면 2만 있는 파티에서도 이야기 X)
// 진실을 아는 사람들과 파티로 연결되어 있다면 이야기 X
// 몇 명의 사람들이 진실을 아는 사람과 같은 집합에 있는지 - union find