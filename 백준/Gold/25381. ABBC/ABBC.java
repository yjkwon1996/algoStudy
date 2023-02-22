import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static Deque<Integer> Aqueue = new ArrayDeque<>(); // A 문자열의 인덱스를 저장
    static Deque<Integer> Bqueue = new ArrayDeque<>(); //  B 문자열의 인덱스를 저장
    static int res = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();

        // B C 먼저 제거 후
        // A B 제거
        for (int i=0; i<S.length(); i++) {
            // A를 만나면
            if (S.charAt(i) == 'A') {
                Aqueue.addLast(i);
            } else if (S.charAt(i) == 'B') { // B를 만나면
                    Bqueue.addLast(i);
            } else if (S.charAt(i) == 'C') { // C 를 만나면
                if ( !Bqueue.isEmpty() && Bqueue.getFirst() < i ) { // 앞에서 만난 B가 있는지 확인 후
                    Bqueue.pollFirst(); // 있으면 제거
                    res++; // 결과값증가
                }
            }
        }

        // B C 를 제거하면서 A를 큐에 넣어뒀으므로 A B만 제거
        while ( !Aqueue.isEmpty() && !Bqueue.isEmpty() ) {
            if ( Aqueue.getFirst() < Bqueue.getFirst() ) { // A B 순서로 되있으면 제거
                res++;
                Aqueue.pollFirst();
                Bqueue.pollFirst();
            } else { // B가 A보다 앞에 있다면 B 제거 후 다음 A B 확인
                Bqueue.pollFirst();
            }
        }
        System.out.println(res);
    }
}
