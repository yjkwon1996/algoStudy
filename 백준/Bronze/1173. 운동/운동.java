import java.io.*;
import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 운동할 시간
        int m = Integer.parseInt(st.nextToken()); // 초기 맥박
        int M = Integer.parseInt(st.nextToken()); // 최대 맥박
        int T = Integer.parseInt(st.nextToken()); // 운동 후 추가되는 맥박수치
        int R = Integer.parseInt(st.nextToken()); // 휴식 후 감소되는 맥박수치

        int answer = 0; // 현재시간
        int time = 0; // 운동시간
        int now = m; // 현재 맥박

        if (now+T > M && now-R < m) {
            System.out.println(-1);
            return;
        }

        while (time < N) {
            answer++;
            if (now+T <= M) {
                now += T;
                time++;
            } else {
                now -= R;
                if(now < m) {
                    now = m;
                }
            }

        }

        System.out.println(answer);

    }
}
