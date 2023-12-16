import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N, M;
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int cnt = 0;
        String [] arr = new String [N];
        for(int i=0; i<N; i++) {
            arr[i] = br.readLine();
            if (!arr[i].contains("X")) {
                cnt++;
            }
        }

        int cnt2 = 0;
        boolean flag;
        for (int i=0; i<M; i++) {
            flag = true;
            for (int j=0; j<N; j++) {
                if (arr[j].charAt(i) == 'X') {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                cnt2++;
            }
        }

        System.out.println(Math.max(cnt, cnt2));

    }
}
