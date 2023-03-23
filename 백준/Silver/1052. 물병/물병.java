import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        if (N <= K) { // 이미 K개를 넘지 않음 - 물병을 살 필요 없음
            System.out.println(0);
            return;
        }

        int cnt = 0; // 산 개수
        int amount = 0;
        while (true) {
            amount = 0;
            int another = N; // N개의 물병을 합치는 중
            while(another != 0) { 
                if (another%2 == 1) { // 홀수인 경우
                    amount++;
                }
                another = another / 2;
            }

            if (amount <= K) { // 전체 물병 수가 K개 이하가 됐다면 끝
                break;
            }
            N++; // 없으면, 물병을 하나 추가 후 다시 찾기
            cnt++;
        }

        System.out.println(cnt);

    }
}

// 같은 양을 한쪽으로 몰아넣기
// 같은 양이 없으면 1리터짜리 새 물병을 살 수 있음
// 이런 방식으로 K개를 넘지 않는 비어있는 물병 만들기
