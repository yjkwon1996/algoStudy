import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N, M;
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int [] P = new int[M];
        for(int i=0; i<M; i++) {
            int value = Integer.parseInt(br.readLine());
            P[i] = value;
        }

        Arrays.sort(P);
        int value = 0;
        int answer = 0;
        for(int i=0; i<M; i++) {
            int sum = 0;
            if(M-i < N) {
                sum = P[i] * (M-i);
            } else {
                sum = P[i] * N;
            }
            if (answer < sum) {
                value = P[i];
                answer = sum;
            }
        }

        System.out.println(value + " " + answer);

    }
}
