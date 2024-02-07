import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int graph[][];
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		graph = new int [100][100];
		for (int l = 0; l<N; l++) {
			
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			for (int i = x; i<x + 10 ; i++) {
				for (int j = y; j<y+10; j++) {
					graph[i][j] = 1;
				}
			}
		}
		int ans= 0;
		for (int i = 0; i<100 ; i++) {
			for (int j = 0; j<100; j++) {
				if(graph[i][j]==1) {
					ans ++;
				}
			}
		}
		System.out.println(ans);

	}

}