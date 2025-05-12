import java.util.*;
import java.awt.*;
class Solution {
    static Queue<Point> q;
    static int[][] visited;
    static int N, M;
    static int dx[] = {-1,1,0,0};
    static int dy[] = {0,0,-1,1};
    
    public int solution(int[][] maps) {
        q = new LinkedList<>();
        N = maps.length;
        M = maps[0].length;
        
        visited = new int[N][M];
        q.offer(new Point(0,0));
        visited[0][0] = 1;
        
        while (!q.isEmpty()){
            Point p = q.poll();
            int x = p.x;
            int y = p.y;
            //System.out.println(x + " " + y);
            for (int i = 0;i < 4; i ++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= N || ny >= M || nx < 0 || ny < 0 ) continue;
                if (maps[nx][ny] == 1 && visited[nx][ny] == 0 ){
                    visited[nx][ny] = visited[x][y] + 1;
                    q.offer(new Point (nx, ny));
                }
            }
        }
        if (visited[N-1][M-1] == 0)return -1;
        else return visited[N-1][M-1];
    }
    
}