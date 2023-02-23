import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int arr [][];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r1 = Integer.parseInt(st.nextToken());
        int c1 = Integer.parseInt(st.nextToken());
        int r2 = Integer.parseInt(st.nextToken());
        int c2 = Integer.parseInt(st.nextToken());

        arr = new int[r2-r1+1][c2-c1+1]; // 배열의 크기
        // 배열을 다 채워야 하나? -> 아닌거같은데
        // 필요한 위치의 필요한 값들만 찾아서 리턴
        // 출력시 공백을 포함한 모든 숫자의 길이가 같아야 함( 출력 할 두 자리 숫자가 있다면 "1" -> " 1") -> 출력할 최대 숫자를 파악
        int max = 0;
        for (int i=r1; i<=r2; i++) {
            for (int j=c1; j<=c2; j++) {
                arr[i-r1][j-c1] = findLocation(i, j);
                max = Math.max(max, arr[i-r1][j-c1]);
            }
        }

        // StringBuilder -> %3d -> 3자리수 만들기, %5d -> 5자리수 만들기. %(max)d -> max 자리수 만들기(printf에서만 가능)
        StringBuilder sb = new StringBuilder("%");
        sb.append(String.valueOf(max).length());
        sb.append("d ");

        for(int i=0; i<=r2-r1; i++){
            for(int j=0; j<=c2-c1; j++){
                System.out.printf(sb.toString(), arr[i][j]);
            }
            System.out.println();
        }

    }

    // r과 c를 입력받아서 몇 번째 테두리인지 찾고, (r,c)의 수를 리턴
    public static int findLocation(int r, int c) {
        int border = Math.max( Math.abs(r), Math.abs(c) ); // 몇 번째 테두리인지
        int min = (int) Math.pow(2*border-1, 2) + 1; // 그 테두리의 최솟값. (0,0)을 첫 번째 테두리로 가정하기 때문에 (2n-3)^2+1이 아님

        if(r == border){ // 테두리 아래에 위치한 경우 최소값 + 7n - 1 + 열값
            return min + 7*border -1 + c;
        } else if(c == -border){ // 테두리 왼쪽에 위치한 경우 최소값 + 5n - 1 + 행값
            return min + 5*border -1 + r;
        } else if(r == -border){ // 테두리 위쪽에 위치한 경우 최소값 + 3n - 1 - 열값
            return min + 3*border -1 - c;
        } else { // 테두리 우측에 위치한 경우 최소값 + n - 1 - 행값
            return min + border -1 - r;
        }

    }
}

// 1
// 2 3 4 5 6 7 8 9 -> (2n-3)^2+1 ~ (2n-1)^2
// 10 ~ 25 -> (2n-3)^2+1 ~ (2n-1)^2
// 오른쪽부터 시작
