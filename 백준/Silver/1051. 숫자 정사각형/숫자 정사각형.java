import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int arr[][];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];

        for (int i=0; i<N; i++) {
            String s = br.readLine();
            for (int j=0; j<M; j++) {
                arr[i][j] = s.charAt(j) - '0';
            }
        }

        int size = Math.min(N, M); // 정사각형의 사이즈(길이)

        while (size > 1) {
            for (int i=0; i<=N-size; i++) {
                for (int j=0; j<=M-size; j++) {
                    int value = arr[i][j]; // 꼭지점의 값들을 비교
                    if (arr[i][j+size-1] == value && arr[i+size-1][j] == value && arr[i+size-1][j+size-1] == value) {
                        System.out.println(size*size); // 꼭지점이 동일한 최대 크기를 찾으면 출력 후 종료
                        return;
                    }
                }
            }
            size--;
        }

        System.out.println(1); // 없으면 1출력
    }
}
