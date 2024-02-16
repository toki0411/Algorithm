import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M, D;
	static int graph[][], graph2[][];
	static int dx[] = {0,-1,0};
	static int dy[] = {-1,0,1};
	static int ans;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        graph = new int [N+1][M];
        graph2 = new int [N+1][M];
        
        for (int i = 0; i < N; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j = 0; j < M; j++) {
        		graph[i][j] = Integer.parseInt(st.nextToken());
        		graph2[i][j] = graph[i][j];
        	}
        }
        
        for (int i = 0; i < M; i ++) {
        	for (int j = i+1; j < M; j ++) {
        		for (int k = j+1; k < M; k++) {
        			int val = 0;
        			for (int l = 0; l < N; l++) {
        				for (int ll = 0; ll < M; ll ++) {
        					graph[l][ll] = graph2[l][ll];
        				}
        			}
        			for (int l = 0; l < N; l++) {
        				boolean flag = false;
	        			for (int o = 0; o < N; o++) {
	        				for (int q =0; q < M; q++) {
	        					if (graph[o][q] == 1) {
	        						flag = true;
	        					}
	        				}
	        			}
	        			if (!flag) {
	        				break;
	        			}
	        			Point p1 = bfs(i);
	        			Point p2 = bfs(j);
	        			Point p3 = bfs(k);
	        			if(p1.x != -1 && p1.y != -1) {
	        				graph[p1.x][p1.y] = 0; 
	        				val ++;
	        			}
	        			if (p2.x != -1 && p2.y != -1 &&graph[p2.x][p2.y] == 1 ) {
	        				graph[p2.x][p2.y] = 0; 
	        				val ++;
	        			}
	        			if (p3.x != -1 && p3.y != -1 &&graph[p3.x][p3.y] == 1 ) {
	        				graph[p3.x][p3.y] = 0; 
	        				val ++;
	        			}
	        			move();
        			}
        			ans = Math.max(val, ans);
        		}
        	}
        }
       System.out.println(ans);
	}
	private static void move() {
		for (int i = N-2; i >=0 ; i--) {
			for (int j = 0; j < M; j++) {
				graph[i+1][j] = graph[i][j];
				graph[i][j] = 0;
			}
		}
	}
	private static Point bfs(int bow) {
		Queue<Point> queue = new LinkedList<Point>();
		queue.offer(new Point(N, bow));
		boolean visited[][] = new boolean[N][M];

		while (!queue.isEmpty()) {
			Point p = queue.poll();
//			System.out.println(p.x);
			for(int i = 0; i < 3; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				if (nx >= 0 && ny >= 0 && nx < N && ny < M && graph[nx][ny] == 1 && Math.abs(nx - N)+Math.abs(ny-bow) <= D && !visited[nx][ny]) {  //표적을 찾음 
					
					visited[nx][ny] = true;
					return new Point(nx,ny);
				}
				else if(nx >= 0 && ny >= 0 && nx < N && ny < M && graph[nx][ny] == 0 && Math.abs(nx - N)+Math.abs(ny-bow) <= D && !visited[nx][ny]) {
					visited[nx][ny] = true;
					queue.offer(new Point(nx,ny));	
					
				}
			}
		}
		return new Point(-1,-1);
		
	}
	
	private static class Point{
		int x;
		int y;
		
		public Point(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}

}