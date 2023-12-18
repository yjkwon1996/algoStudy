import java.io.*;
import java.lang.*;
import java.util.*;

public class Main {

    static boolean visited [];
    static int T, N, answer;
    static int [] arr;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for(int t=0; t<T; t++) {
            answer = 0;
            N = Integer.parseInt(br.readLine());
            arr = new int[N];
            visited = new boolean[N];
            st = new StringTokenizer(br.readLine());


            for(int i=0; i<N; i++) {
                arr[i] = Integer.parseInt(st.nextToken()) - 1;
            }

            for(int i=0; i<N; i++) {
                if (!visited[i]) {
                    answer++;
                    dfs(i);
                }
            }

            System.out.println(answer);
        }
    }

    static void dfs(int s) {
        visited[s] = true;

        int next = arr[s];
        if (!visited[next]) {
            dfs(arr[s]);
        }
    }
}
