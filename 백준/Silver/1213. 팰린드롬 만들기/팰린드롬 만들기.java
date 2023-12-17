import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int [] num = new int[26];

        // 팰린드롬 : 앞뒤가 똑같음 -> 개수를 세어 봤을 때 홀수가 2개 이상이면 안됨
        String s = br.readLine();
        for(int i=0; i<s.length(); i++) {
            num[s.charAt(i) - 'A']++;
        }

        int cnt = 0;
        for(int i=0; i<26; i++) {
            if (num[i] % 2 != 0) cnt++;
        }

        StringBuilder sb = new StringBuilder();
        String answer = "";
        if (cnt > 1) {
            System.out.println("I'm Sorry Hansoo");
            return;
        }

        for (int i=0; i<26; i++) {
            for (int j=0; j<num[i]/2; j++) {
                sb.append((char)(i + 'A'));
            }
        }
        answer += sb.toString();
        String end = sb.reverse().toString();

        sb = new StringBuilder();
        for(int i=0; i<26; i++) {
            if (num[i] % 2 == 1) {
                sb.append((char)(i+65));
            }
        }
        answer += sb.toString() + end;

        System.out.println(answer);


    }
}
