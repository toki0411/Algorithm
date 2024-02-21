import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static int graph[][];
	static int dir[][][] = {
		    {},
		    {{0}, {1}, {2}, {3}},
		    {{0, 2}, {1, 3}},
		    {{0, 1}, {1, 2}, {2, 3}, {3, 0}},
		    {{0, 1, 3}, {0, 1, 2}, {1, 2, 3}, {2, 3, 0}},
		    {{0, 1, 2, 3}}
		};
	static int dx [] = {-1,0,1,0};
	static int dy[] = {0,1,0,-1};
	static ArrayList <Cctv> cctv;
	static int minVal = 1000;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		cctv = new ArrayList<>();
		graph = new int[n][m];
		for (int i  = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0 ; j < m; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] != 0 && graph[i][j] != 6) {
					cctv.add(new Cctv(graph[i][j], i,j));
				}
			}
		}
		
		dfs(0, graph);
		System.out.println(minVal);
		
	}
	private static void dfs(int depth, int[][] graph) {
		if (depth == cctv.size()) {
			int val = 0;
			for (int i = 0; i < n; i++) {
				for (int j  = 0; j < m; j++) {
					if (graph[i][j] == 0) {  //사각지대의 개수를 카운트
						val ++;
					}
				}
			}
			minVal = Math.min(val, minVal);
			return;
		}
		
		int cctvNum=cctv.get(depth).num;
		int cctvX=cctv.get(depth).x;
		int cctvY=cctv.get(depth).y;
		for (int i =0; i <dir[cctvNum].length; i++) {
			//기존 배열 복사 
			int [][]tmp = new int[n][m];
			for (int k = 0; k < n; k++) {
				for (int j  = 0; j < m; j++) {
					tmp[k][j] = graph[k][j];
				}
			}
			
			monitoring(dir[cctvNum][i], tmp, cctvX, cctvY);  //cctv의 번호를 가지고 각각의 방향을 결정 후, 얼마나 모니터링 할 수 있는지 체크 
			dfs(depth+1, tmp);
		}
		
	}
	private static void monitoring(int[] d, int [][] graph, int x, int y) { //{0, 1, 3}
		for (int i =0; i < d.length; i++) {
			int nx = x ;
			int ny = y;
			while (true) {
				nx += dx[d[i]];
				ny += dy[d[i]];
				
				if (nx >= n || ny >=m || nx <0 || ny <0 ) {
					break;
				}
				else if (graph[nx][ny] == 6) {
					break;
				}
				else {
					graph[nx][ny] = graph[x][y];
				}
			}
		}
		
	}
	public static class Cctv{
		int num;
		int x;
		int y;
		public Cctv(int num, int x, int y) {
			super();
			this.num = num;
			this.x = x;
			this.y = y;
		}
		
	}

}