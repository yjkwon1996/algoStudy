import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int minPack = Integer.MAX_VALUE; // 제일 싼 것만 기억
        int minSingle = Integer.MAX_VALUE;
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int tmpPack = Integer.parseInt(st.nextToken()); // 6개가 1패키지
            int tmpSingle = Integer.parseInt(st.nextToken());

            minPack = Math.min(tmpPack, minPack);
            minSingle = Math.min(tmpSingle, minSingle);
        }
        
        int ans = Math.min( ((N/6)+1)*minPack, N*minSingle ); // 패키지로만 사는 경우와 단일로만 사는 경우
        ans = Math.min(ans, (N/6)*minPack + (N%6)*minSingle); // 혹은 섞어서 사는 경우에서 가장 싼 경우를 찾기

        System.out.println(ans);

    }
}

// N개 이상을 사기 위해 필요한 최소한의 돈