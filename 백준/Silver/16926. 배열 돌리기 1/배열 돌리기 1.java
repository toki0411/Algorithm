import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m, r;
	static int arr[][];
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		
		for (int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int k = 0; k < r; k++) {
			for (int l = 0; l < Math.min(n, m) / 2; l++) {
				int tmp;
				//아래
				int value = arr[l][l];
				for (int i = l+1; i < n-l; i++) {
					tmp = arr[i][l];
					arr[i][l] = value;
					value = tmp;
				}
				
				//오른쪽
				for (int i = l+1; i < m-l; i++) {
					tmp = arr[n-l-1][i];
					arr[n-l-1][i] = value;
					value = tmp;
				}
				
				//위로
				for (int i = n-l-2; i > l-1 ; i--) {
					tmp = arr[i][m-1-l];
					arr[i][m-1-l] = value;
					value = tmp;
				}
				
				//왼쪽
				for (int i = m-l-2; i > l-1; i--) {
					tmp = arr[l][i];
					arr[l][i] = value;
					value = tmp;
				}

			}
			
		}
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<m; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
	}

}