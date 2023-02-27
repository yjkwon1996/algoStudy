import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int [][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        int ans = -1;

        for (int i=0; i<N; i++) { // 행 열
            String inputValue = br.readLine();
            for (int j=0; j<M; j++) {
                arr[i][j] = inputValue.charAt(j) - '0';
            }
        }
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                for (int mi = -N; mi < N; mi++) {
                    for (int mj = -M; mj < M; mj++) {
                        if (mi == 0 && mj == 0) { // 둘다 움직이지 않을 때
                            continue;
                        }

                        int t = 0;
                        int newI = i;
                        int newJ = j;
                        while (newI >= 0 && newI < N && newJ >= 0 && newJ < M) // 배열 범위 내 
                        {
                            t = 10 * t + arr[newI][newJ]; // 기존에 담긴 숫자가 있다면 *10해주고 더하기
                            if (Math.abs(Math.sqrt(t) - (int) Math.sqrt(t)) < 1e-10) { // 완전 제곱수인지 판별
                                ans = Math.max(ans, t);
                            }
                            newI += mi;
                            newJ += mj;
                        }
                    }
                }
            }
        }
        System.out.println(ans);
//        for(int i=0; i<N; i++) {
//            for (int j=0; j<M; j++) {
//                System.out.println(arr[i][j]);
//            }
//        }


    }
}

// 왼쪽 아래에서 위로 올라가는 형태
// 왼쪽 위에서 아래로 내려가는 형태
// 오른쪽 아래에서 위로 올라가는 형태
// 오른쪽 위에서 아래로 내려가는 형태
// 행만 움직이는 형태
// 열만 움직이는 형태