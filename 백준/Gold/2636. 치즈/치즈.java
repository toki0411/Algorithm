import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M;
	static int graph[][];
	static int dx [] = {-1,1,0,0};
	static int dy[] = {0,0,-1,1};
	static boolean visited [][] ;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new int [N][M];
		for (int i =0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j ++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int t = 0; 
		int lastCheese = checkCheese();
		int prevCheese = 0;
		if (lastCheese==0) {
			System.out.println(t);
			System.out.println(lastCheese);
		}
		else {
			while (true) {
				visited = new boolean[N][M];
				bfs(0,0);
				prevCheese = lastCheese;
				lastCheese = checkCheese();
				melted();
				if (lastCheese == 0) {
					System.out.println(t);
					System.out.println(prevCheese);
					break;
				}
				t++;
			}
			
			
		}
	}
	private static void melted() {
		for (int i = 0 ; i < N; i ++) {
			for (int  j = 0; j < M; j++) {
				if (visited[i][j] && graph[i][j] == 1) {
					graph[i][j] = 0;
				}
			}
		}
	}
	private static int checkCheese() {
		int count = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (graph[i][j] == 1) {
					count ++;
				}
			}
		}
		return count;
	}
	private static void bfs(int x, int y) {
		Queue<Point> q = new LinkedList<>();
		q.add(new Point(x,y));
		
		while (!q.isEmpty()) {
			Point p = q.poll();
			for (int i = 0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				
				if (nx >= N || ny >= M || nx < 0 || ny < 0) {
					continue;
				}
				else if (graph[nx][ny] == 1 && !visited[nx][ny]) {
					visited[nx][ny] = true;
				}
				else if (graph[nx][ny] == 0 && !visited[nx][ny]) {
					visited[nx][ny] = true;
					q.add(new Point(nx,ny));
				}
			}
			
		}
		
	}

}