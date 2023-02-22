import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int dp [][] = new int [41][2]; // 0 1
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        dp[0][0] = 1; // 0번째 피보나치수의 0 출력 수 : 1
        dp[0][1] = 0; // 0번때 피보나치수의 1 출력 수 : 0
        dp[1][0] = 0; // 1번째 피보나치수의 0 출력 수 : 0
        dp[1][1] = 1; // 1번째 피보나치수의 1 출력 수 : 1

        for (int t=0; t<testCase; t++) {
            int N = Integer.parseInt(br.readLine());

            for (int i=2; i<=N; i++) {
                dp[i][0] = dp[i-1][0] + dp[i-2][0];
                dp[i][1] = dp[i-1][1] + dp[i-2][1];
            }

            System.out.println(dp[N][0] +" "+dp[N][1]);

        }
    }
}
