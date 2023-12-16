import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String [] student = new String [N];
//        int [] result = new int[N];

        for(int i=0; i<N; i++) {
            student[i] = br.readLine();
        }

        int length = student[0].length();
        Set<Integer> result;
        for(int i=0; i<length; i++) {
            result = new HashSet<>();
            for (int j=0; j<N; j++) {
//                System.out.println(Integer.parseInt(student[j].substring(length-i-1, length-i)));
                result.add(Integer.parseInt(student[j].substring(length-i-1, length)));
            }
            if (result.size() == N) {
                System.out.println(i+1);
                return;
            }
        }


    }
}
