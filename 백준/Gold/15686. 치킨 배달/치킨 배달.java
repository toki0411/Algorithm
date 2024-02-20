import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	private static final int MAX = 1000000;
	static int graph[][];
	static int N, M;
	static boolean visited[][];
	static int dx [] = {-1,1,0,0};
	static int dy[] = {0,0,-1,1};
	static int ans;
	static ArrayList<Point> chickenIdx;
	static ArrayList<Point> houseIdx;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		graph = new int [N][N];
		chickenIdx = new ArrayList<>();
		houseIdx = new ArrayList<>();
		visited = new boolean[N][N];
		for (int i = 0; i < N; i ++ ) {
			st = new StringTokenizer(br.readLine());
			for (int j =0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if(graph[i][j] == 2)chickenIdx.add(new Point(i,j));
				else if (graph[i][j] == 1) houseIdx.add(new Point(i,j));
			}
		}
		ans = MAX;
		dfs(0,0);
		System.out.println(ans);
		
		
	}
	private static void dfs(int start, int cnt) {
		if (cnt == M) {
			calChickenDistance();
			return; 
		}
		for (int i = start; i < chickenIdx.size(); i++) {
			int x = chickenIdx.get(i).x;
			int y = chickenIdx.get(i).y;
			visited[x][y] = true;
			dfs(i+1, cnt + 1);
			visited[x][y] = false;
			dfs(i+1, cnt);
		}
		
	}
	private static void calChickenDistance() {
		int [][] distance = new int [N][N];
		for (int i =0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				distance[i][j] = MAX;
			}
		}
				
		for (int i =0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				
				if (visited[i][j]) {
					for (int k = 0; k < houseIdx.size(); k++) {
						Point p = houseIdx.get(k);
						distance[p.x][p.y] = Math.min(Math.abs(p.x - i) + Math.abs(p.y - j), distance[p.x][p.y]);
					}
				}
			}
		}
		int val = 0;
		for (int i =0; i < houseIdx.size(); i++) {
			Point p = houseIdx.get(i);
			val += distance[p.x][p.y];
		}
		ans = Math.min(val, ans);
		
	}
	
	
}