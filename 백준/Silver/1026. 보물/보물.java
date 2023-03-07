import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static int A [];
    static Integer B [];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        A = new int[N];
        B = new Integer [N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(A);
        Arrays.sort(B, Collections.reverseOrder());

        int sum = 0;
        for (int i=0; i<N; i++) {
            sum += A[i]*B[i];
        }

        System.out.println(sum);
    }
}

// S = A[0] × B[0] + ... + A[N-1] × B[N-1] 을 가장 작게 만들기 위해 A를 재배열
// B를 재배열하면 안되지만, 결과는 최솟값만을 보여주기 때문에 계산에는 상관X
// 가장 큰 수와 가장 작은 수를 곱하도록
