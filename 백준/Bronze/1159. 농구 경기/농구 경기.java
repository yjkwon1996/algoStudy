import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int [] arr = new int[26];

        boolean flag = false;
        for(int i=0; i<N; i++) {
            String s = br.readLine();
            char c = s.charAt(0);
            arr[c-97]++;
            if (arr[c-97] == 5) flag = true;
        }

        StringBuilder sb = new StringBuilder();
        if (flag) {
            for(int i=0; i<26; i++) {
                if (arr[i] >= 5) {
                    sb.append((char)(i+97));
                }
            }
        } else {
            sb.append("PREDAJA");
        }
        System.out.println(sb);

    }
}
