import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int dx[] = {0,1,0,-1};
		int dy[] = {1,0,-1,0};
		int t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= t; tc++) {
			int n = Integer.parseInt(br.readLine());
			System.out.println("#" + tc);
			int arr[][] = new int[n][n];
			int x = 0; int y = 0;
			int idx = 0;
			arr[0][0] = 1;
			
			for (int i=2; i<= n*n; i++) {
				int nx = x + dx[idx];
				int ny = y + dy[idx];
				if (nx < n && ny < n && nx >=0 && ny >=0 && arr[nx][ny]==0) {
				}
				else {
					idx += 1;
					if (idx == 4)idx = 0;
					nx = x + dx[idx];
					ny = y + dy[idx];
				}
				
				x = nx;
				y = ny;
				arr[x][y] = i;
		
			}
			
			for (int i = 0; i< n; i++) {
				for (int j =0; j<n; j++) {
					System.out.print(arr[i][j] + " ");
				}
				System.out.println();
			}
		}
	}

}