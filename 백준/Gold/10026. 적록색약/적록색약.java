import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static char[][] graph;
	static int dx [] = {-1,1,0,0};
	static int dy[] = {0,0,-1,1};
	static boolean [][] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		graph = new char[N][N];
		for (int i = 0; i < N; i++) {
			char arr[] = br.readLine().toCharArray();
			for (int j = 0; j < N; j++) {
				graph[i][j] = arr[j];
			}
		}
		
		visited = new boolean[N][N];
		int normal = 0; 
		for (int i =0; i < N; i++ ) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					bfs(i,j);
					normal ++;
				}
			}
		}
		
		visited = new boolean[N][N];
		int colorBlind = 0;
		for (int i =0; i < N; i++ ) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					colorBlindBfs(i,j);
					colorBlind ++;
				}
			}
		}
		
		System.out.println(normal + " " + colorBlind);
	}
	private static void colorBlindBfs(int x, int y) {
		Queue<Point> q = new LinkedList<>();
		q.add(new Point(x,y));
		while (!q.isEmpty()) {
			Point p = q.poll();
			
			for (int i = 0; i < 4; i++ ) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				
				if (nx >= N || ny >= N || nx < 0 || ny < 0) {
					continue;
				}
				if (!visited[nx][ny]) {
					if (graph[nx][ny] == graph[x][y]) {
						visited[nx][ny] = true;
						q.add(new Point(nx, ny));
					}
					else if (graph[x][y] == 'R' && graph[nx][ny] == 'G') {
						visited[nx][ny] = true;
						q.add(new Point(nx, ny));
					}
					else if (graph[x][y] == 'G' && graph[nx][ny] == 'R') {
						visited[nx][ny] = true;
						q.add(new Point(nx, ny));
					}
				}
				
			}
		}
	}
	private static void bfs(int x, int y) {
		Queue<Point> q = new LinkedList<>();
		q.add(new Point(x,y));
		while (!q.isEmpty()) {
			Point p = q.poll();
			for (int i = 0; i < 4; i++ ) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				
				if (nx >= N || ny >= N || nx < 0 || ny < 0) {
					continue;
				}
				if (graph[nx][ny] == graph[x][y] && !visited[nx][ny]) {
					visited[nx][ny] = true;
					q.add(new Point(nx, ny));
				}
			}
		}
		
	}
	
	

}