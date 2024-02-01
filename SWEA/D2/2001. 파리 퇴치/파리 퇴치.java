import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int T,N,M;
	static int [][] arr;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		StringTokenizer st;

		for (int tc = 1; tc<=T; tc ++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			arr = new int[N+1][N+1];
			
			
			for (int i = 1; i<N+1; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 1; j < N+1; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			//행 더하기 
			for (int i = 1; i<N+1; i++) {
				for (int j = 1; j < N; j++) {
					arr[i][j+1] += arr[i][j];
				}
			}
			//열 더하기 
			for (int i = 1; i<N+1; i++) {
				for (int j = 1; j < N; j++) {
					arr[j+1][i] += arr[j][i];
				}
			}
			int max_val = 0;
			for (int i = M; i < N+1; i++) {
				for (int j = M; j <N+1; j++) {
					int val = arr[i][j] - arr[i-M][j] - arr[i][j-M] + arr[i-M][j-M];
					if (val > max_val) {
						max_val = val;
					}
				}
			}

			System.out.println("#" + tc + " " + max_val);
		}
		
		
	}

}