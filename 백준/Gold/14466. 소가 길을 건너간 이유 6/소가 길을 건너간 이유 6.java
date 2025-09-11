
import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, K, R;
    static ArrayList<Point>[][] road;	//길 저장 배열
    static int visited[][];
    static ArrayList<Point> cow;
    static int dx[] = {0, 0, 1, -1};
    static int dy[] = {1, -1, 0, 0};
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        road = new ArrayList[N+1][N+1];
        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++)
                road[i][j] = new ArrayList<>();
        }

        visited = new int [N+1][N+1];
        cow = new ArrayList<>();
        ans = 0;
        for (int i = 0; i < R; i ++) {
            st = new StringTokenizer(br.readLine());
            int r1 = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());

            int r2 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());
            road[r1][c1].add(new Point(r2, c2));
            road[r2][c2].add(new Point(r1, c1));
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            cow.add(new Point(x,y));
        }

        for (int i = 0; i< cow.size(); i++){
            for (int j = i+1; j < cow.size(); j ++) {
                bfs(cow.get(i), cow.get(j));
            }
        }
        System.out.println(ans);

    }
    static void bfs(Point p1, Point p2) {
        for (int i = 0; i < N+1; i++){
            for (int j = 0; j< N+1; j++){
                visited[i][j] = 0;
            }
        }
        boolean key = false;
        Queue<Point> q = new LinkedList<>();
        q.add(p1);
        visited[p1.x][p1.y] = 1;
        while (!q.isEmpty()){
            Point p = q.poll();
            if (p.x == p2.x && p.y == p2.y){
                key = true;
                break;
            }
            //System.out.print(p.x + " " + p.y + " ");
            for (int i = 0; i < 4; i ++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                boolean flag = true;
                if (nx <= 0 || ny <= 0 || nx >= N +1 || ny >= N+1)continue;
                for (int j = 0; j < road[p.x][p.y].size(); j ++) {
                    if (road[p.x][p.y].get(j).x == nx && road[p.x][p.y].get(j).y == ny ){
                        flag = false;
                        break;
                    }
                }
                if (flag == true && visited[nx][ny] == 0){
                    visited[nx][ny] = 1;
                    q.add(new Point(nx, ny));
                }
            }
        }
        if (key == false) {
            ans ++;
        }
    }
}
