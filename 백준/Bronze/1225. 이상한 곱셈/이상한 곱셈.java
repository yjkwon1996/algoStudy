import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String A;
        String B;

        StringTokenizer st = new StringTokenizer(br.readLine());
        A = st.nextToken();
        B = st.nextToken();

        long sum = 0;
        for(int i=0; i<A.length(); i++) {
            for(int j=0; j<B.length(); j++) {
                sum += (A.charAt(i) - '0') * (B.charAt(j) - '0');
            }
        }
        System.out.println(sum);

    }
}
