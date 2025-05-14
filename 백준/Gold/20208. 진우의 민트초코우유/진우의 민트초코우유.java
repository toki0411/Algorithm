import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

import static java.lang.Long.sum;
import static java.lang.Math.abs;
import static java.lang.Math.max;

public class Main {

    static int N,M,H;
    static int sx, sy;
    static int graph[][];
    static List<Point> milk;
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        milk = new ArrayList<>();
        sx= 0; sy= 0;
        ans = 0;
        graph = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 1) {
                    sx = i; sy = j;
                }
                else if (graph[i][j] == 2) {
                    milk.add(new Point(i, j));
                }
            }
        }
        dfs(sx, sy, M, 0);
        System.out.println(ans);

    }
    static void dfs(int x, int y, int hp, int mCnt){
        for (int i = 0; i < milk.size(); i++) {
            int nx = milk.get(i).x;
            int ny = milk.get(i).y;
            if (graph[nx][ny] == 2) {
                int dist = Math.abs(x - nx) + Math.abs(y - ny);
                if (dist <= hp) {
                    graph[nx][ny] = 0;
                    dfs(nx, ny, hp - dist + H, mCnt + 1);
                    graph[nx][ny] = 2;
                }
            }
        }
        int hdist = Math.abs(x - sx) + Math.abs(y - sy);
        if (hdist <= hp) {
            ans = Math.max(mCnt, ans);
        }

    }
}