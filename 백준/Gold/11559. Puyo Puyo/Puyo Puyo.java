import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {-1, 0, 1, 0};
    static boolean [][] visited;
    static char [][] arr = new char[12][6];
    static ArrayList<Node> list;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int i=0; i<12; i++) {
            String s = br.readLine();
            for(int j=0; j<6; j++) {
                arr[i][j] = s.charAt(j);
            }
        }

        // 같은 색 뿌요가 상하좌우로 4개 이상 모이면 없어짐.
        Queue<Node> q;
        int answer = 0;
        while(true) {
            boolean flag = true;
            visited = new boolean[12][6];

            for(int i=0; i<12; i++) {
                for(int j=0; j<6; j++) {
                    if (arr[i][j] != '.') {
                        list = new ArrayList<>();
                        bfs(i, j, arr[i][j]);

                        if(list.size() >= 4) {
                            flag = false;
                            for(int k=0; k<list.size(); k++) {
                                arr[list.get(k).x][list.get(k).y] = '.';
                            }
                        }

                    }
                }
            }
            if(flag) break;
            fall();
            answer++;
        }
        System.out.println(answer);
    }

    public static void bfs(int x, int y, char c) {
        visited[x][y] = true;
        Queue<Node> q = new LinkedList<>();
        list.add(new Node(x, y));
        q.offer(new Node(x, y));

        while(!q.isEmpty()) {
            Node now = q.poll();
            for(int d=0; d<4; d++) {
                int nx = now.x + dx[d];
                int ny = now.y + dy[d];

                if(nx>=0 && nx<12 && ny>=0 && ny<6 && visited[nx][ny] == false && arr[nx][ny] == c) {
                    visited[nx][ny] = true;
                    list.add(new Node(nx, ny));
                    q.offer(new Node(nx, ny));
                }
            }
        }

    }

    public static void fall() {
        for(int i=0; i<6; i++) {
            for(int j=11; j>0; j--) {
                if (arr[j][i] == '.') {
                    for(int k=j-1; k>=0; k--) {
                        if (arr[k][i] != '.') {
                            arr[j][i] = arr[k][i];
                            arr[k][i] = '.';
                            break;
                        }
                    }
                }
            }
        }
    }

    public static class Node {
        int x, y;
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
