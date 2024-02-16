import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static int N,M,V;
	static boolean adjMatrix[][];
	static boolean visited[];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt(); M = sc.nextInt(); V = sc.nextInt();
		adjMatrix = new boolean[N+1][N+1];
		for (int i =0; i < M; i ++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			adjMatrix[a][b] = true;
			adjMatrix[b][a] = true;
		}
		
		visited = new boolean[N+1];
		dfs(V, visited);
		System.out.println();
		bfs(V);
		

	}
	private static void bfs(int current) {
		Queue<Integer> queue = new LinkedList<Integer>();
		boolean visited[] = new boolean[N+1];
		queue.offer(current);
		visited[current] = true;
		
		while (!queue.isEmpty()) {
			current = queue.poll();
			System.out.print(current+" ");
			for(int i = 0; i < N+1; i++) {
				if(adjMatrix[current][i] && !visited[i]) {
					queue.offer(i);
					visited[i] = true;
				}
			}
		}
	}
	
	public static void dfs(int current, boolean[] visited) {
		visited[current] = true;
		System.out.print(current+" ");
		for (int i = 0; i < N+1; i++) {
			if(adjMatrix[current][i] && !visited[i]) {
				dfs(i, visited);
			}
		}
	}
}