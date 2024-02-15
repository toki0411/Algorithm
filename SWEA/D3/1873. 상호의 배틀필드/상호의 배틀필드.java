
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static int T, H, W, N;
    static char[][] graph;
    static char[] cmd;
    static int tank_x, tank_y;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            H = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());

            graph = new char[H][W];
            for (int i = 0; i < H; i++) {
                String line = br.readLine();
                for (int j = 0; j < W; j++) {
                    graph[i][j] = line.charAt(j);
                    if (graph[i][j] == '>' || graph[i][j] == '^' || graph[i][j] == 'v'
                            || graph[i][j] == '<') {
                        tank_x = i;
                        tank_y = j;
                    }
                }
            }
            N = Integer.parseInt(br.readLine());
            cmd = br.readLine().toCharArray();

            for (int i = 0; i < N; i++) {
                int nx = tank_x;
                int ny = tank_y;

                switch (cmd[i]) {
                    case 'U':
                        graph[nx][ny] = '^';
                        nx -= 1;
                        if (nx >= 0 && nx < H && graph[nx][ny] == '.') {
                            graph[nx + 1][ny] = '.';
                            graph[nx][ny] = '^';
                            tank_x = nx;
                        }
                        break;
                    case 'D':
                        graph[nx][ny] = 'v';
                        nx += 1;
                        if (nx >= 0 && nx < H && graph[nx][ny] == '.') {
                            graph[nx - 1][ny] = '.';
                            graph[nx][ny] = 'v';
                            tank_x = nx;
                        }
                        break;
                    case 'L':
                        graph[nx][ny] = '<';
                        ny -= 1;
                        if (ny >= 0 && ny < W && graph[nx][ny] == '.') {
                            graph[nx][ny + 1] = '.';
                            graph[nx][ny] = '<';
                            tank_y = ny;
                        }
                        break;
                    case 'R':
                        graph[nx][ny] = '>';
                        ny += 1;
                        if (ny >= 0 && ny < W && graph[nx][ny] == '.') {
                            graph[nx][ny - 1] = '.';
                            graph[nx][ny] = '>';
                            tank_y = ny;
                        }
                        break;
                    case 'S':
                        if (graph[nx][ny] == '>') {
                            shoot(nx, ny, 0, 1);
                        } else if (graph[nx][ny] == '^') {
                            shoot(nx, ny, -1, 0);
                        } else if (graph[nx][ny] == 'v') {
                            shoot(nx, ny, 1, 0);
                        } else if (graph[nx][ny] == '<') {
                            shoot(nx, ny, 0, -1);
                        }
                        break;
                }
            }
            System.out.print("#" + tc + " ");
            for (int i = 0; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    System.out.print(graph[i][j]);
                }
                System.out.println();
            }
        }
    }

    private static void shoot(int x, int y, int dx, int dy) {
        x = x + dx;
        y = y + dy;
        while (true) {
            if (x < 0 || y < 0 || x >= H || y >= W) {
                return;
            }
            if (graph[x][y] == '#') {
                return;
            } else if (graph[x][y] == '*') {
                graph[x][y] = '.';
                return;
            }
            x = x + dx;
            y = y + dy;
        }
    }
}