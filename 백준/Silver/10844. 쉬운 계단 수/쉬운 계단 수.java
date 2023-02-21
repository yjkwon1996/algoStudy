import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;

public class Main {

    static long dp[][];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        dp = new long[N+1][10]; // 길이가 N+1이고 && 0 ~ 9 10자리수로 시작하는 숫자인 경우


        for (int i=0; i<=9; i++) {
            dp[1][i] = 1L; // 길이가 1일 때는 계단 수의 개수만
        }

        for (int i=2; i<=N; i++) {
            dp[i][0] = dp[i-1][1]; // 길이가 i일 때 0으로 시작하는 수에서 dp[i][0]는 dp[i-1][1]과 동일
            for (int j=1; j<=9; j++) {
                if (j == 9) { // 길이가 i이고 9로 시작하는 수는 dp[i-1][8]과 동일
                    dp[i][9] = dp[i-1][8] % 1000000000;
                } else {
                    // 이전 숫자의 j-1로 시작하는 수와 j+1로 시작하는 수의 개수를 더한 값
                    dp[i][j] = (dp[i-1][j-1] % 1000000000 + dp[i-1][j+1] % 1000000000) % 1000000000;
                }
            }
        }
        long res = 0;
        for (int i=1; i<=9; i++) {
            res = (res + dp[N][i]) % 1000000000;
        }
        System.out.println(res);

    }
}
