import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int sumValue = 0;
        StringBuilder sb = new StringBuilder();
        while (true) {
            if (L > 100) {
                sb.append(-1);
                break;
            }
            int first = (N / L) - ((L - 1) / 2);
            if ( first < 0 ) {
                L++;
                continue;
            }
            sumValue = 0;
            for (int i = first; i < first + L; i++) {
                sumValue += i;
            }
            if (sumValue == N) {
                for (int i = first; i < first + L; i++) {
                    sb.append(i).append(" ");
                }
                break;
            } else {
                L += 1;
            }
        }
        System.out.println(sb);

    }
}

// 18 2 -> 5 6 7
// 18 / 2 는 안됨
// 18 / 3 = 6. 처음 시작하는 수는 6 - (길이 - 1 / 2) : 6 - (3-1 / 2) = 5
// 18 4 -> 3 4 5 6
// 18 / 4 = 4. 처음 시작하는 수는 4 - (길이 - 1 / 2) : 4 - (4-1 / 2) = 3
// 45 10 -> 0 1 2 3 4 5 6 7 8 9
// 45 / 10 -> 4. 처음 시작하는 수는 4 - (길이 - 1 / 2) : 4 - (10-1 / 2) = 0


