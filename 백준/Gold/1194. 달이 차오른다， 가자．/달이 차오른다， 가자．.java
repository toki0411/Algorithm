import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static char[][] graph;
    static int[][][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[] keyMap = {1, 2, 4, 8, 16, 32};
    static int[] doorMap = {1, 2, 4, 8, 16, 32};

    static class Point {
        int x, y, key, dis;

        public Point(int x, int y, int key, int dis) {
            this.x = x;
            this.y = y;
            this.key = key;
            this.dis = dis;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new char[N][M];
        visited = new int[N][M][64];

        for (int i = 0; i < N; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < M; j++) {
                graph[i][j] = line.charAt(j);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (graph[i][j] == '0') {
                    graph[i][j] = '.';
                    System.out.println(bfs(i, j));
                }
            }
        }
    }

    public static int bfs(int x, int y) {
        Queue<Point> queue = new ArrayDeque<>();
        queue.add(new Point(x, y, 0, 0));
        visited[x][y][0] = 1;

        while (!queue.isEmpty()) {
            Point point = queue.poll();
            x = point.x;
            y = point.y;
            int key = point.key;
            int dis = point.dis;

            if (graph[x][y] == '1') {
                return dis;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    continue;
                }
                if (visited[nx][ny][key] == 0) {
                    if (graph[nx][ny] == '1' || graph[nx][ny] == '.') {
                        visited[nx][ny][key] = 1;
                        queue.add(new Point(nx, ny, key, dis + 1));
                    } else if (graph[nx][ny] >= 'a' && graph[nx][ny] <= 'f') {
                        int num = keyMap[graph[nx][ny] - 'a'];
                        int tmpKey = key | num;
                        visited[nx][ny][tmpKey] = 1;
                        queue.add(new Point(nx, ny, tmpKey, dis + 1));
                    } else if (graph[nx][ny] >= 'A' && graph[nx][ny] <= 'F') {
                        int num = doorMap[graph[nx][ny] - 'A'];
                        int val = key & num;
                        if (val != 0) {
                            visited[nx][ny][key] = 1;
                            queue.add(new Point(nx, ny, key, dis + 1));
                        }
                    }
                }
            }
        }
        return -1;
    }
}