import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int tc=0; tc<t; tc++) {
            int n = Integer.parseInt(br.readLine());
            HashMap<String, Integer> have = new HashMap();
            for (int i=0; i<n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                String kind = st.nextToken();
                if (have.containsKey(kind)) { // 기존의 옷종류라면 값추가
                    have.put(kind, have.get(kind)+1);
                } else { // 새로 들어왔으면 등록
                    have.put(kind, 1);
                }
            }
            // 경우의 수( kind개의 종류 중 1개만, 2개만, ... kind개만 입을 경우의 수)
            int res = 1;
            for (int value : have.values()) {
                res = res * (value + 1); //  안입는 경우 포함
            }
            System.out.println(res-1); // 다 벗은 경우는 빼야됨
        }
    }
}
