import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static ArrayList<ArrayList<Integer>> graph;
	static boolean[] visited;
	static boolean key;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		graph = new ArrayList<>();
		
		for (int i = 0; i < n; i++) {
			graph.add(new ArrayList<>());
		}
		
	
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			graph.get(a).add(b);
			graph.get(b).add(a);	
		}
		
		key = false;
		visited = new boolean[n];
		for (int i =0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				visited[j] = false;
			}
			visited[i] = true;
			dfs(0, i);
			if (key) {
				break;
			}
		}
		
		if (key) System.out.println(1);
		else System.out.println(0);
	}
	
	private static void dfs(int depth, int cur) {
		if (depth == 4) {
			key = true;
			return;
		}
		
		for (int i = 0; i < graph.get(cur).size(); i++) {
			int nx = graph.get(cur).get(i);
			if (!visited[nx]) {
				visited[nx] = true;
				dfs(depth+1, nx);
				visited[nx] = false;
			}
		}
	}
}