import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static int N, S;
	static int graph[][];
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st ;
		
		for (int tc = 1; tc <= 10; tc ++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			S = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			graph = new int[101][101];
			for (int i = 0; i < N; i+=2) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				
				graph[from][to] = 1;
			}
			
			Queue <Integer> q = new LinkedList<>();
			int[] visited = new int[101];
			int cnt = 0;
			visited[S] = 1;
			q.add(S);
			while (!q.isEmpty()) {
				int x = q.poll();
				
				for (int i = 1; i < 101; i++) {
					if (visited[i]==0 && graph[x][i] == 1) {
						visited[i] = visited[x]+1;
						q.add(i);
						cnt = visited[i]; 
					}
				}
			}
			for (int i = 100; i >= 0; i--) {
				if (visited[i] == cnt) {
					System.out.println("#"+ tc + " " + i);
					break;
				}
			}
			
		}
	}

}