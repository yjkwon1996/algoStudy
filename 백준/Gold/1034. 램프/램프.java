import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static String [] line;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        line = new String[N];

        for (int i=0; i<N; i++) {
            line[i] = br.readLine(); // 문자열 형식으로 저장해서 나중에 동일한 패턴을 찾기 쉽도록
        }
        int K = Integer.parseInt(br.readLine());
        int sniffling = K % 2; // K의 홀짝 여부
        if (K > 50) { // 열 갯수가 50개이므로, 50번 이상은 의미가 없음
            K = 50;
        }

        int max = 0;

        for (int i=0; i<N; i++) {
            int zero = 0; // 행에서 0의 갯수 파악
            for (int j=0; j<M; j++) {
                if (line[i].charAt(j) == '0') {
                    zero++;
                }
            }

            if (zero > K) { // 0의 갯수가 K보다 많으면 다음으로
                continue;
            }

            int samePattern = 1; // 1은 자기 자신
            if ( zero%2 == sniffling ) { // K와의 홀짝이 동일하다면 계속 진행
                for (int j=0; j<N; j++) {
                    if ( i != j && line[i].equals(line[j]) ) { // 다른 동일한 패턴 찾기
                        samePattern++;
                    }
                }
            } else { // 홀짝이 다르면 다음 행으로
                continue;
            }
            if (samePattern > max) {
                max = samePattern;
            }
        }

        // 모든 행을 돌면서 찾았음
        System.out.println(max);

    }
}

// 열마다 스위치가 있고, 스위치를 누르면 그 열에서 켜져있는 스위치는 꺼지고 꺼져있으면 켜짐
// 스위치를 K번 눌렀을 때 램프가 켜져있는 행의 최대값 - 홀짝
// 각 행에서 0의 갯수와 K의 수에서, 둘의 홀짝이 동일하다면 켤 수 있는 것이고
// 켤 수 있는 동일한 패턴이 몇개인지 찾음 - 그 중 최댓값을 출력
// 모든 행렬을 탐색 후 K개의 열의 램프를 바꿨을 때 가장 많은 행의 램프가 켜졌을 때 그 행의 수를 출력