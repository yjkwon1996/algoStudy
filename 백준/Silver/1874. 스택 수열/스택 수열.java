import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        int lastValue = 1;
        StringBuilder sb = new StringBuilder();
        boolean flag = true;
        for (int i=1; i<=n; i++) {
            int value = Integer.parseInt(br.readLine());

            if (value > lastValue) { // 입력받은 값이 더 크면 그 수까지 push 진행후 pop
                while (lastValue <= value) {
                    sb.append("+").append("\n");
                    stack.push(lastValue++);
                }
                stack.pop();
                sb.append("-").append("\n");
            } else if (value < lastValue) { // 더 작으면 마지막 스택 값을 확인 후 다르다면 No
                if (stack.peek() == value) {
                    stack.pop();
                    sb.append("-").append("\n");
                } else {
                    flag = false;
                    System.out.println("NO");
                    return;
                }
            } else { // 동일할 때
                sb.append("+").append("\n");
                sb.append("-").append("\n");
                stack.push(lastValue++);
                stack.pop();
            }

        }
        if (flag) {
            System.out.println(sb.toString());
        }

    }
}
