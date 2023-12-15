import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int S1, S2, S3;
        int sum;
        int [] result = new int [83];

        StringTokenizer st = new StringTokenizer(br.readLine());
        S1 = Integer.parseInt(st.nextToken());
        S2 = Integer.parseInt(st.nextToken());
        S3 = Integer.parseInt(st.nextToken());

        for(int i=1; i<=S1; i++ ) {
            for (int j=1; j<=S2; j++) {
                for (int k=1; k<=S3; k++) {
                    sum = i + j + k;
                    result[sum]++;
                }
            }
        }

        int maxNum = 0;
        int answer = 0;
        for(int i=0; i<80; i++) {
            if (result[i] > maxNum) {
                maxNum = result[i];
                answer = i;
            }
        }
        System.out.println(answer);

    }
}
