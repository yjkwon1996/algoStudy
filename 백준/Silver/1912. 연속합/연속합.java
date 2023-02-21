import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int arr [];
    static int dp [];
    static int maxValue = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N];
        dp = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        dp[0] = arr[0];
        for (int i=1; i<N; i++) { // dp[i] 는 i번까지의 연속합 중 최대값
            dp[i] = Math.max(dp[i-1] + arr[i], arr[i]);
        }
        for (int i=0; i<N; i++) {
            maxValue = Math.max(maxValue, dp[i]);
        }
        System.out.println(maxValue);

    }
}
