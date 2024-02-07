import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static int graph[][];
	static int T,N;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,1,-1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		T = Integer.parseInt(st.nextToken());
		Queue<Pos> q;
		
		for (int tc = 1; tc <= T; tc ++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			Pos ansIdx = new Pos(0,0);
			int ans = 0;
			graph = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					int val = 1;
					q = new LinkedList<>();
					q.add(new Pos(i,j));
					
					while (!q.isEmpty()) {
						Pos p = q.poll();
						int x = p.x;
						int y = p.y;
						for (int k = 0; k < 4; k ++) {
							int nx = x + dx[k];
							int ny = y + dy[k];
							if (nx >=0 && ny >=0 && nx < N && ny < N && graph[nx][ny] == graph[x][y]+1) {
								q.add(new Pos(nx,ny));
								val ++;
							}
						}
					}
					if (val > ans) {
						ans = val;
						ansIdx = new Pos(i,j);	
					}
					else if (val == ans) {
						if (graph[i][j] < graph[ansIdx.x][ansIdx.y]) {
							ans = val;
							ansIdx = new Pos(i,j);
						}
					}
				}
			}
			int xIdx = ansIdx.x;
			int yIdx = ansIdx.y;
//			if (xIdx == -1 && yIdx == -1) System.out.println("#"+tc+" "+1+" " + ans);
			System.out.println("#"+tc+" "+graph[xIdx][yIdx]+" " + ans);
			
		}
	}
	static class Pos {
		int x;
		int y;
		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}

}