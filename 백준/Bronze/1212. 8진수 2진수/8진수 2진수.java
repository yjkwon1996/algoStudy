import java.io.*;
import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int N = Integer.parseInt(br.readLine(), 8);
//        System.out.println(Integer.toBinaryString(N));

        String [] arr = {"000", "001", "010", "011", "100", "101", "110", "111"};
        String s = br.readLine();

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length(); i++) {
            int value = s.charAt(i) - '0';
            sb.append(arr[value]);
        }

        if (s.equals("0")) {
            System.out.println(s);
        } else {
            while (sb.charAt(0) == '0') { // 앞자리 0 제거
                sb = new StringBuilder(sb.substring(1));
            }
            System.out.println(sb);
        }



    }
}
