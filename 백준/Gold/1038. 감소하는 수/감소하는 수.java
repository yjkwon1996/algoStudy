import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static List<Long> list = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int ans = 0;
        if (N <= 10) { // 10 이하는 그대로
            System.out.println(N);
        } else if (N >= 1023) {
            System.out.println(-1);
        } else {
            for (int i=0; i<10; i++) {
                DFS(i, 1);
            }
            Collections.sort(list);
            System.out.println(list.get(N));
        }

    }

    static void DFS(long num, int idx) {
        if (idx > 10) { // 10자리수
            return;
        }

        list.add(num);
        for (int i=0; i<num%10; i++) {
            DFS((num*10)+i, idx+1);
        }
    }
}

// 0 ~ 9로 10자리 숫자를 만드는 방법은 2^10 = 1024. 아무것도 선택하지 않는 경우를 제외 -> 1023
// % 연산으로 10배수씩 계산, 자신은 포함하지 않기
// 각 리스트별로 시작하는 자릿수에서 나올 수 있는 내림수를 담아서, 그 수를 찾아서 뽑아냄
// (i, j) i로 시작하는 j번째 내림수
