import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int k;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int t=0; t<testCase; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            k = 0;
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            // y-1 -> y가 마지막에 항상 성립해야 함.
            int dist = y-x;
            int max = (int) Math.sqrt(dist); // 최대 속도는 거리의 제곱근
            if (max == Math.sqrt(dist) ) { // 최대 거리
                System.out.println(max*2-1);
            } else if (max * max + max >= dist) { // max에서 max+1로 넘어가는 구간은 max 값만큼해서 2개의 구간으로 나뉨.
                System.out.println(max * 2);
            } else {
                System.out.println(max * 2 + 1);
            }
        }

    }
}

//        1 1                       1
//        2	1 1
//        3	1 1 1
//        4	1 2 1		            2*2-1   3  max 구간
//        5	1 2 1 1                         4   2   1
//        6	1 2 2 1                         4   2   2
//        7	1 2 1 2 1                       5   2   1
//        8	1 2 2 2 1                       5   2   2
//        9	1 2 3 2 1	        	3*2-1   5   3
//        10	1 2 3 2 1 1                 6
//        ...
//        16	1 2 3 4 3 2 1 	    4*2-1
