import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static final int INF = 10000000;
	static int H, W, K;
	static int graph[][];
	static int ans;
	static int[] horseDx = {-1, -2, -2, -1, 1, 2, 2, 1}; // 말 점프
	static int[] horseDy = {-2, -1, 1, 2, 2, 1, -1, -2}; 
	static int dx [] = {-1,1,0,0};
	static int dy [] = {0,0,1,-1};
	static boolean [][][] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		K = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());  //가로
		H = Integer.parseInt(st.nextToken());  //세로
		graph = new int[H][W];
		visited = new boolean[H][W][K+1];
		for (int i = 0; i < H; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < W; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(bfs());
	
	}
	private static class Monkey {
		int x;
		int y;
		int cnt;
		int horseCnt;
		public Monkey(int x, int y, int cnt, int horseCnt) {
			super();
			this.x = x;
			this.y = y;
			this.cnt = cnt;
			this.horseCnt = horseCnt;
		}
	}
	private static int bfs() {
		Queue <Monkey> q = new LinkedList<>();
		q.add(new Monkey(0,0,0,0));
		visited[0][0][0] = true;
		while (!q.isEmpty()) {
			Monkey m = q.poll();
			if (m.x == H-1 && m.y == W-1) {
				return m.cnt;
			}
			for (int i = 0; i < 4; i++) {
				int nx = m.x + dx[i];
				int ny = m.y + dy[i];
				if (nx < 0 || ny < 0 || nx >= H || ny >= W) continue;
				if (!visited[nx][ny][m.horseCnt] && graph[nx][ny] == 0) {
					q.add(new Monkey(nx, ny, m.cnt+1, m.horseCnt));
					visited[nx][ny][m.horseCnt] = true;
				}
			}
			if (m.horseCnt < K) {
				for (int i = 0; i < 8; i++) {
					int nx = m.x + horseDx[i];
					int ny = m.y + horseDy[i];
					if (nx < 0 || ny < 0 || nx >= H || ny >= W) continue;
					if (!visited[nx][ny][m.horseCnt+1] && graph[nx][ny] == 0) {
						q.add(new Monkey(nx, ny, m.cnt+1, m.horseCnt+1));
						visited[nx][ny][m.horseCnt+1] = true;
					}
				}
			}
			
		}
		return -1;
	}
}