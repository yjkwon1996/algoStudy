import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int newPoint = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        int arr [] = new int[N];

        if (N == 0) {
            System.out.println(1);
            return;
        }

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;
        int ans = 1; //  등수
        for (int i=0; i<N; i++) {
            if (newPoint < arr[i]) {
                ans += 1;
            } else if ( newPoint > arr[i] ) {
                break;
            }
            cnt++;
        }

        if (cnt == P) ans = -1;
        if (N == 0) ans = 1;

        System.out.println(ans);
    }

}
