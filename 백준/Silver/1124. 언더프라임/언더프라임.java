import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    static int A, B;
    static boolean [] prime = new boolean[100001];
    static int [] cnt = new int[100001];
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        prime[0] = true;
        prime[1] = true;

        for (int i=2; i<100001; i++) {
            if(prime[i]) continue;
            for(int j=i*2; j<100001; j+=i) {
                prime[j] = true;
                int tmp = j;
                while(tmp%i == 0) {
                    tmp = tmp / i;
                    cnt[j]++;
                }
            }
        }

        int answer = 0;
        for(int i=A; i<=B; i++) {
            if(!prime[cnt[i]]) {
                answer++;
            }
        }

        System.out.println(answer);

    }
}
