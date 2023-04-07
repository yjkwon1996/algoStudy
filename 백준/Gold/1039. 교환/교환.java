import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, K, ans = -1;
    static int visited [] = new int[1000001]; // 이미 계산한 수를 여기에
    static Queue<Integer> queue = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int length = (int)(Math.log10(N)+1);

        queue.add(N);

        while ( !queue.isEmpty() && K>0) { // K번 연산하면 멈춰야함
            int size = queue.size();

            for (int x=0; x<size; x++) {
                int p = queue.poll();

                for (int i=0; i<length-1; i++) {
                    for (int j=i+1; j<length; j++) {
                        int value = change(p, i, j);

                        if (value == 0 || visited[value] == K ) continue; // 앞자리가 0이거나 이미 방문했으면 다음으로
                        // 아니면 큐에 추가
                        queue.add(value);
                        visited[value] = K;
                    }
                }

            }
            K--;
        }

        if ( !queue.isEmpty() ) { // 큐에 넣어둔 값들을 비교
            for (int x : queue) {
                ans = Math.max(x, ans);
            }
        }
        System.out.println(ans);

    }

    public static int change(int now, int i, int j) {
        char [] str = String.valueOf(now).toCharArray();

        char tmp = str[i];
        str[i] = str[j];
        str[j] = tmp;

        if (str[0] == '0') { // 제일 앞자리가 0이면 안됨
            return 0;
        }
        return Integer.parseInt(new String(str)); // 바꾼 숫자 리턴
    }
}
