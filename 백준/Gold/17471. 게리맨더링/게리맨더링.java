import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[] population;
	static ArrayList<ArrayList<Integer>> graph;
	static boolean[] visited;
	static int ans=10000000;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		population = new int[N+1];
		
		graph = new ArrayList<>();
		graph.add(new ArrayList<>());
		
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i < N+1; i++) {
			population[i] = Integer.parseInt(st.nextToken());
			graph.add(new ArrayList<>());
		}
		
		visited = new boolean[N+1];
		for (int i = 1; i < N+1; i++) {
			st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			for (int j = 0; j < num; j++) {
				int a = Integer.parseInt(st.nextToken());
				graph.get(i).add(a);
			}
		}
		
		for (int i = 1; i < N/2+1; i++) {
			visited = new boolean[N+1];
			dfs(i,0);
		}
		
		if (ans == 10000000) {
			System.out.println(-1);
		}
		else {
			System.out.println(ans);
		}
		
	}

	private static void dfs(int n, int cnt) {
		if (cnt == n) {
			List<Integer> A = new LinkedList<>();
			List<Integer> B = new LinkedList<>();
			for (int i = 1; i < N+1; i++) {
				if (visited[i]) {
					A.add(i);
				}
				else {
					B.add(i);
				}
			}
			int a = bfs(A);
			int b = bfs(B);
//			System.out.println(Arrays.deepToString(A.toArray()));

			if (a == -1 || b == -1) {
				return;
			}
			ans = Math.min(Math.abs(a-b), ans);
			return;
		}
		for (int i = 1; i < N+1; i ++) {
//			System.out.println(i);
			if (!visited[i]) {
				visited[i] = true;
				dfs(n, cnt + 1);
				visited[i] = false;
			}
		}
	}
	
	private static int bfs(List<Integer> arr) {
		Queue <Integer> q = new LinkedList<>();
		q.add(arr.get(0));
		boolean []visited2 = new boolean[N+1];
		visited2[arr.get(0)] = true;
		int cnt = 1;
		int value = population[arr.get(0)];
		
		while (!q.isEmpty()) {
			int x = q.poll();
			for (int i = 0; i < arr.size(); i++) {
				if (!visited2[arr.get(i)] && graph.get(x).contains(arr.get(i)) ) {
					q.add(arr.get(i));
					cnt ++;
					visited2[arr.get(i)] = true;
					value += population[arr.get(i)];
				}
			}
		}
		
		if (cnt == arr.size()) {
			return value;
		}
		else return -1;
	}

	
}