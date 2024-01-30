
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	

	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		for (int tc = 1; tc <= 10; tc ++) {
			int graph[][] = new int[100][100];
			br.readLine();
			
			boolean visited[][] = new boolean[100][100];
			int x = 0;
			int y = 0;
			
			for (int i=0; i< 100; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j<100; j++) {
					int k = Integer.parseInt(st.nextToken());
					graph[i][j] = k;
					if (k == 2) {
						x = i;
						y = j;
					}
				}
			}
			int dx[] = {0,0,-1};
			int dy[] = {-1,1,0};
			int ans = 0;
			
			while (true) {
				
				if (x == 0 && graph[x][y] == 1) {
					ans = y;
					break;
				}
				for (int i=0; i<3; i++) {
					int nx = x + dx[i];
					int ny = y + dy[i];
					if (0<=nx && 0<=ny && nx < 100 && ny < 100 && graph[nx][ny] == 1 && !visited[nx][ny]) {
						x = nx;
						y = ny;
						visited[nx][ny] = true;
						break;
					}
					
				}
			}

			System.out.println("#"+tc+" " + ans);
		}

	}

}
