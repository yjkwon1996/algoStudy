import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int building [];
    static int res []; // res[i] : i번 건물에서 보이는 건물의 갯수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        building = new int[N];
        res = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            building[i] = Integer.parseInt(st.nextToken());
        }

        // 탐색 시작
        for (int i=0; i<N-1; i++) {
            res[i]++; // 바로 오른쪽 건물
            res[i+1]++; // A에서 B가 보이듯 B에서도 A가 보임

            double gradient = building[i+1] - building[i]; // 높이 X, 기울기를 비교해야함

            for (int j=i+2; j<N; j++) { // i번 건물 오른쪽 두번째 건물부터 시작
                double nextGradient = (double)(building[j] - building[i]) / ( j - i ); // double 타입 명시
                if ( nextGradient > gradient ) { // 새로운 건물의 기울기가 이전 건물들보다 더 큰게 있다면 서로 보인다는 뜻
                    gradient = nextGradient;
                    res[i]++;
                    res[j]++;
                }
            }
        }
        // 가장 많은 빌딩이 보이는 경우를 출력
        int max = Integer.MIN_VALUE;
        for (int i=0; i<N; i++) {
            max = Math.max(max, res[i]);
        }

        System.out.println(max);
    }
}

// 가장 많은 빌딩이 보이는 빌딩을 구하고 거기서 보이는 빌딩의 수 출력
// 건물 기준 탐색. A에서 B가 보이면 B에서도 A가 보임
// queue??? 아니면
// 한쪽 방향만 확인하면서 기억하면 될듯
// 0부터 N-1까지 돌면서 오른쪽 건물만 체크
