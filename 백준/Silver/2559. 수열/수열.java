import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int [] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        int end = 0;
        int maxValue = Integer.MIN_VALUE;
        int nowValue = 0;
        for (int i=0; i<N; i++) {
            if (i-end >= K) {
                if (maxValue < nowValue) {
                    maxValue = nowValue;
                }
                nowValue -= arr[end];
                end++;
            }
            arr[i] = Integer.parseInt(st.nextToken());
            nowValue += arr[i];
        }
        if (maxValue < nowValue) { // 마지막 값까지 계산
            maxValue = nowValue;
        }
        System.out.println(maxValue);
    }
}
