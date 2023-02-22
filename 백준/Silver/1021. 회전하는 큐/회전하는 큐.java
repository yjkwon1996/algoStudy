import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static LinkedList<Integer> deque = new LinkedList<>();
    static int cnt = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        for (int i=1; i<=N; i++) { // N까지 넣어주고
            deque.add(i);
        }

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<M; i++) {
            int find = Integer.parseInt(st.nextToken()); // 찾아야 하는 수
            int idx = deque.indexOf(find); // 위치를 찾아서

            if (deque.peekFirst() == find) {
                deque.pollFirst();
                continue;
            }
            // 중간보다 앞이면 2번연산
            if ( idx <= deque.size() / 2 ) {
                int tmp = idx;
                for (int j=0; j<tmp; j++) {
                    int out = deque.pollFirst();
                    deque.addLast(out);
                    cnt++;
                }
            } else {// 뒤면 3번연산
                int tmp = (deque.size()) - idx;
                for (int j=0; j<tmp; j++) {
                    int out = deque.pollLast();
                    deque.addFirst(out);
                    cnt++;
                }
            }
            // 이후 첫 값 제거
            deque.pollFirst();

        }
        System.out.println(cnt);
    }
}

//        1 2 3 4 5 6 7 8 9 10
//        1 2 3
//
//        2 9 5
//        1 - 2 3 4 5 6 7 8 9 10 1 -> 3 4 5 6 7 8 9 10 1
//        2 - 1 3 4 5 6 7 8 9 10
//        3 - 10 1 3 4 5 6 7 8 9
//        4 - 9 10 1 3 4 5 6 7 8 -> 10 1 3 4 5 6 7 8
//        5 - 8 10 1 3 4 5 6 7
//        6 - 7 8 10 1 3 4 5 6
//        7 - 6 7 8 10 1 3 4 5
//        8 - 5 6 7 8 10 1 3 4 -> 6 7 8 10 1 3 4