import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int graph[][];
	static int dp[][];
	static int ans;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		graph = new int[N][N];
		dp = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		ans = 0;
		dfs(0,1,0);
		System.out.println(ans);
	}
	private static void dfs(int x, int y, int pos) {
		if (x == N-1 && y == N-1) {
			ans++;
			return;
		}
		if (pos == 0 || pos == 2) {  //가로
			int ny = y + 1;
			if (ny < N && graph[x][ny] == 0) 
				dfs(x, y+1, 0);
		}
		if (pos == 1 || pos == 2) { //세로 
			int nx = x + 1;
			if (nx < N && graph[nx][y] == 0) 
				dfs(x+1, y, 1);
		}
		//대각선
		if (x + 1 < N && y + 1 < N && graph[x+1][y+1] == 0 && graph[x+1][y] == 0 && graph[x][y+1]==0) {
			dfs(x+1, y+1, 2);
		}
		
	}

}