import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int graph[][];
    static int dp[][][];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        graph = new int[N][N];
        dp = new int[N][N][3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp[0][1][0] = 1;
        for (int i = 2; i < N; i++) {
            if (graph[0][i] == 0)
                dp[0][i][0] = dp[0][i-1][0];
        }
        System.out.println(dp());
        //System.out.println(Arrays.deepToString(dp));

    }
    private static int dp() {
        for (int i = 1; i < N; i++) {
            for (int j = 2; j < N; j++) {
                if (graph[i][j] == 1) continue;
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2];
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2];
                if (graph[i-1][j] ==0 && graph[i][j-1] == 0)
                    dp[i][j][2] = dp[i-1][j-1][0]+ dp[i-1][j-1][1] + dp[i-1][j-1][2];
            }
        }

        return dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2];
    }

}