import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static Queue<Integer> queue = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        for (int i=1; i<=N; i++) {
            queue.add(i);
        }

        int flag = 0;
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        while ( !queue.isEmpty() ) {
            flag++;
            int tmp = queue.poll(); // 꺼내고
            if (flag == K) { // K 번째면 끝
                flag = 0;
                sb.append(tmp).append(", ");
                continue;
            }
            queue.add(tmp); // K 번째가 아니면 다시 넣어주고
        }
        sb.delete(sb.length()-2, sb.length());
        sb.append(">");
        System.out.println(sb);
    }
}
