import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.NumberFormat;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] arr = new int[6];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Integer.parseInt(br.readLine()); // 얘도 long이어야함...

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 6; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        long ans = 0;
        long v1 = 4;
        long v2 = 4 * (N-1) + 4 * (N-2);
        long v3 = 4 * (N-1) * (N-2) + (N-2) * (N-2);
        long tmp1 = Math.min(arr[0], arr[5]);
        long tmp2 = Math.min(arr[1], arr[4]);
        long tmp3 = Math.min(arr[2], arr[3]);
        long min1 = Math.min(tmp1, Math.min(tmp2, tmp3)); // 셋 중 가장 작은 값
        long min2 = Math.min(tmp1 + tmp2, Math.min(tmp1 + tmp3, tmp2 + tmp3)); // 마주보는 두 값을 더했을 때의 최솟값
        long min3 = tmp1 + tmp2 + tmp3; // 세 면이 드러났을 때
        if (N == 1) { // 최대값 제외 모두 더하기
            int max = Integer.MIN_VALUE;
            for (int i = 0; i < 6; i++) {
                ans += arr[i];
                max = Math.max(max, arr[i]);
            }
            ans -= max;
            System.out.println(ans);
        } else {
            ans = v1*min3 + v2*min2 + v3*min1;
            System.out.println(ans);
        }
    }
}

// N * N * N = N^3
// 보이는 곳의 크기 : 앞뒤옆위( 5 * (N*N) )
// 하나의 주사위가 세 군데에서 보이는 경우 : 4
// 하나의 주사위가 두 군데에서 보이는 경우 : 8 * (N-2) + 4
// 하나의 주사위가 한 군데에서 보이는 경우 : ( 5 * (N-2)*(N-2) ) + 4 * (N-2)
// 단순하게?
// 4 * (N-1) + 4 * (N-2)
// 4 * (N-1) * (N-2) + (N-2) * (N-2)
// 중복되는 범위도 생각
// 최솟값 3개를 찾아서 각각 더하면 될듯?
// 2개, 3개일 때 주사위 도면을 생각해서 맞는 값이 들어갈 수 있도록 해야 함
// 마주보는 면의 인덱스 합은 5
