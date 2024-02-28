import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    private static final int INF = 10000000;
    static int T, N;
    static int graph[][];
    static int dx[] = {-1, 1, 0, 0};
    static int dy[] = {0, 0, -1, 1};
    static ArrayList<Point> core;
    static int ans, maxCore;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            graph = new int[N][N];
            core = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                    if (graph[i][j] == 1) {
                        if (i == 0 || j == 0 || i == N - 1 || j == N - 1) continue;
                        else core.add(new Point(i, j));
                    }
                }
            }
            ans = INF;
            maxCore = -1;
            dfs(0,0, 0);
            System.out.println("#" + t + " " + ans);
        }
    }

    private static void dfs(int cnt, int coreCnt, int cost) {
        if (cnt == core.size()) {
            if (coreCnt > maxCore) {
                maxCore = coreCnt;
                ans = cost;
            }
            else if (coreCnt == maxCore) {
                ans = Math.min(cost, ans);
            }
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = core.get(cnt).x + dx[i];
            int ny = core.get(cnt).y + dy[i];
            int val = 0;
            while (nx >= 0 && ny >= 0 && nx < N && ny < N) {
                if (graph[nx][ny] != 0) {
                    val = 0;
                    break;
                }
                val++;
                nx += dx[i];
                ny += dy[i];
            }
            nx = core.get(cnt).x;
            ny = core.get(cnt).y;
            for (int l = 0; l < val; l++) {
                nx += dx[i];
                ny += dy[i];
                graph[nx][ny] = 1;
            }

            if (val == 0) {
                dfs(cnt + 1, coreCnt, cost);
            }
            else {
                dfs(cnt + 1, coreCnt + 1, cost + val);
                nx = core.get(cnt).x;
                ny = core.get(cnt).y;
                for (int l = 0; l < val; l++) {
                    nx += dx[i];
                    ny += dy[i];
                    graph[nx][ny] = 0;
                }
            }

        }

    }
}