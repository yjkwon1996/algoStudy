import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int [] arr = new int[5];
        int cnt = 0;
        int answer = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<5; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        while(true) {
            answer++;
            for(int i=0; i<5; i++) {
                if (answer >= arr[i] && answer % arr[i] == 0) {
                    cnt++;
                }
            }
            if (cnt > 2) break;
            cnt = 0;
        }
        System.out.println(answer);

    }
}
