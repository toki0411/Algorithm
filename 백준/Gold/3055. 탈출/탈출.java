import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int R, C;
	static char graph [][];
	static Point start, goal;
	static int ans;
	static boolean key;
	static int visited [][];
	static int dx[] = {-1,0,1,0};
	static int dy[] = {0,-1,0,1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		graph = new char[R][C];
		
		for (int i = 0; i < R; i++) {
			String line = br.readLine();
			for (int j =0; j < C; j++) {
				graph[i][j] = line.charAt(j);
				if (graph[i][j] == 'D') {
					goal = new Point(i, j);
				}
				else if (graph[i][j] == 'S') {
					start = new Point(i, j);
					graph[i][j] = '.';
				}
			}
		}
		
		bfs(start);
		if (!key) System.out.println("KAKTUS"); 
		
	}
	
	private static void water() {
		Queue <Point> waterQ = new LinkedList<>();
		for (int i = 0; i < R; i ++) {
			for (int j = 0; j < C; j++) {
				if (graph[i][j] == '*') {
					waterQ.add(new Point(i,j));
				}
			}
		}
		
		while (!waterQ.isEmpty()) {
			Point p = waterQ.poll();
			for (int i =0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				
				if (nx < 0 || ny < 0 || nx >= R || ny >= C)continue;
				if (graph[nx][ny] == '.') {
					graph[nx][ny] = '*';
				}
			}
		}
		
	}
	private static void bfs(Point start) {
		Queue <Point> q = new LinkedList<>();
		q.add(start);
		visited = new int[R][C];
		int prev = -1;
		
		while (!q.isEmpty()) {
			Point p = q.poll();
			if(visited[p.x][p.y] > prev) {
				water();
				prev = visited[p.x][p.y];
			}
			for (int i =0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				if (nx < 0 || ny < 0 || nx >= R || ny >= C)continue;
				if (graph[nx][ny] == 'D'&& visited[nx][ny] == 0) {
					System.out.println(visited[p.x][p.y] + 1);
					key = true;
					return;
				}
				else if (graph[nx][ny] == '.' && visited[nx][ny] == 0) {
					q.add(new Point(nx, ny));
					visited[nx][ny] = visited[p.x][p.y] + 1;
				}
			}
		}

	}
	
}