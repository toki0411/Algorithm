import java.util.Scanner;

public class Solution {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] graph;
    static int[][] visited;
    static int[] start;
    static int[] goal;
    static int N;
    static int ans;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            ans = 10000000;
            N = scanner.nextInt();
            graph = new int[N][N];
            visited = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    graph[i][j] = scanner.nextInt();
                    visited[i][j] = ans;
                }
            }
            start = new int[]{scanner.nextInt(), scanner.nextInt()};
            visited[start[0]][start[1]] = 0;
            goal = new int[]{scanner.nextInt(), scanner.nextInt()};
            dfs(start[0], start[1]);
            if (ans == 10000000) {
                System.out.println("#" + tc + " " + -1);
            }
            else {
                System.out.println("#" + tc + " " + ans);
            }


        }
    }

    static void dfs(int x, int y) {
        if (visited[x][y] >= ans) {
            return;
        }
        if (x == goal[0] && y == goal[1]) {
            ans = Math.min(ans, visited[x][y]);
            return;
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
            if (graph[nx][ny] == 0 && visited[nx][ny] > visited[x][y] + 1) {
                visited[nx][ny] = visited[x][y] + 1;
                dfs( nx, ny);

            } else if (graph[nx][ny] == 2) {
                if (visited[x][y] % 3 == 2 && visited[nx][ny] > visited[x][y] + 1) {
                    visited[nx][ny] = visited[x][y] + 1;
                    dfs( nx, ny);

                } else if (visited[x][y] % 3 == 1&& visited[nx][ny] > visited[x][y] + 2) {
                    visited[nx][ny] =  visited[x][y] + 2;
                    dfs( nx, ny);

                } else if (visited[x][y] % 3 == 0 && visited[nx][ny] > visited[x][y] + 3) {
                    visited[nx][ny] =  visited[x][y] + 3;
                    dfs( nx, ny);

                }
            }
        }
    }
}