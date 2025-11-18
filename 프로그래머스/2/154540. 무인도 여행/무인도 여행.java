import java.util.*;
import java.awt.Point;
class Solution {
    static LinkedList<Point> q;
    static char[][] graph;
    static boolean [][] visited;
    static int n, m;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    public ArrayList<Integer> solution(String[] maps) {
        ArrayList <Integer> answer = new ArrayList<>();
        n = maps.length;
        m = maps[0].length();
        graph = new char [n][m];
        visited = new boolean [n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++){
                graph[i][j] = maps[i].charAt(j);
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++){
                if (graph[i][j] != 'X' && !visited[i][j]){
                    answer.add(BFS(new Point(i, j)));
                }
            }
        }
        if (answer.size() == 0) answer.add(-1);
        Collections.sort(answer);
        return answer;
    }
    static int BFS(Point po){
        int cnt = 0;
        q = new LinkedList<>();
        q.offer(po);
        visited[po.x][po.y] = true;
        cnt += (graph[po.x][po.y] - '0');
        while (!q.isEmpty()){
            Point p = q.poll();
            int x = p.x; 
            int y = p.y;
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                //System.out.println(nx + " " + ny);
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (!visited[nx][ny] && graph[nx][ny] != 'X'){
                    visited[nx][ny] = true;
                    q.offer(new Point(nx, ny));
                    cnt += (graph[nx][ny] - '0');
                }
            }
        }
        return cnt;
    }
}