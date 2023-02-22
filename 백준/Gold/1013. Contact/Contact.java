import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        String pattern = "(100+1+|01)+";
        for (int t=0; t<testCase; t++) {
            String input = br.readLine();
            if( input.matches(pattern) ) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }

    }
}

// (100+1+ | 01)+

