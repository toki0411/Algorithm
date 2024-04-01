import java.awt.*;
import java.util.LinkedList;
import java.util.Scanner;

public class Solution {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] graph;
    static int[][] visited;
    static int[] start;
    static int[] goal;
    static int N;


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            N = scanner.nextInt();
            graph = new int[N][N];
            visited = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    graph[i][j] = scanner.nextInt();
                }
            }
            start = new int[]{scanner.nextInt(), scanner.nextInt()};
            goal = new int[]{scanner.nextInt(), scanner.nextInt()};
            int ans = bfs(start[0], start[1]);
            System.out.println("#" + tc + " " + ans);

        }
    }

    static int bfs(int ox, int oy) {
        LinkedList<Node> q = new LinkedList<>();
        q.add(new Node(ox, oy, 0));
        visited[ox][oy]=1;
        int time = 0;
        while (!q.isEmpty()){
            Node p = q.poll();
//            System.out.println(p.x +" " + p.y +" "+ time);
            int x = p.x;
            int y = p.y;
            int t = p.time;
            if (x == goal[0] && y == goal[1]){
                return t;
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                if (visited[nx][ny] == 0 && graph[nx][ny] == 0) {
                    visited[nx][ny] = 1;
                    q.add(new Node(nx, ny, t + 1));
                } else if (visited[nx][ny] == 0 && graph[nx][ny] == 2) {
                    if (t % 3 == 2) {
                        visited[nx][ny] = 1;
                        q.add(new Node(nx, ny, t + 1));
                    } else {
                        q.add(new Node(x, y, t + 1));
                    }
                }
            }

        }
        return -1;

    }
    static class Node {
        int x;
        int y;
        int time;

        public Node(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }

}