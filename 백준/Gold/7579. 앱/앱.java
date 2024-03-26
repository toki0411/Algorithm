import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] memory = new int[n + 1];
        int[] cost = new int[n + 1];
        int limit = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            memory[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
            limit += cost[i]; // 총 cost 계산
        }

        int[][] dp = new int[n + 1][limit + 1];
        int ans = Integer.MAX_VALUE;

        for (int i = 1; i <= n; i++) {
            int mem = memory[i];
            int c = cost[i];
            for (int j = 0; j <= limit; j++) {
                if (j < c) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j - c] + mem, dp[i - 1][j]);
                }
                if (dp[i][j] >= m) {
                    ans = Math.min(ans, j);
                }
            }
        }
        System.out.println(ans);
    }
}