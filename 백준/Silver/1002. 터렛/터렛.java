import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int t=0; t<testCase; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());

            // 두 좌표간의 거리 계산
            int dist = (int)(Math.pow(x1-x2, 2) + Math.pow(y1-y2, 2)); // 중심점간 거리 제곱

            if (x1 == x2 && y1 == y2 && r1 == r2) { // 중점이 같으면서 반지름도 같은 경우
                System.out.println(-1);
            } else if (dist > Math.pow(r1 + r2, 2)) { // 두 원의 반지름 합보다 중점간 거리가 더 먼 경우
                System.out.println(0);
            } else if (dist < Math.pow(r1 - r2, 2)) { // 원 안에 다른 원이 있지만 내접하지 않은 경우
                System.out.println(0);
            } else if (dist == Math.pow(r1 + r2, 2)) { // 외접
                System.out.println(1);
            } else if (dist == Math.pow(r1 - r2, 2)) { // 내접
                System.out.println(1);
            } else { // 그 외의 경우
                System.out.println(2);
            }
        }
    }
}
