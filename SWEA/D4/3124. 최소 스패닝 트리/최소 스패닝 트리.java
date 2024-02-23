import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {
	static class Node implements Comparable<Node> {
		int to;
		int weight;
		
		public Node(int to, int weight) {
			super();
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node n) {
			return this.weight - n.weight;
		}
	}
	
	static int V, E;
	static long ans;
	static int tc;
	static boolean [] visited;
	static ArrayList<Node>[] nodeList;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		tc = Integer.parseInt(st.nextToken());
		
		for (int t = 1; t <= tc; t++) {
			st = new StringTokenizer(br.readLine());
			
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			
			visited = new boolean[V+1];
			nodeList = new ArrayList[V+1];
			ans = 0;
			for (int i = 1; i <= V; i++) {
				nodeList[i] = new ArrayList<>();
			}
			
			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(br.readLine());
				
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				int cost = Integer.parseInt(st.nextToken());
				
				nodeList[from].add(new Node(to, cost));
				nodeList[to].add(new Node(from, cost));
			}
			
			PriorityQueue<Node> pq = new PriorityQueue<>();
			pq.add(new Node(1,0));
			
			while (!pq.isEmpty()) {
				Node n = pq.poll();
				int to = n.to;
				int weight = n.weight;
				
				if (visited[to]) continue;
				visited[to] = true;
				ans += weight;
				
				for (Node next : nodeList[to]) {
					if (!visited[next.to]) pq.add(next);
				}
			}
			System.out.println("#" + t + " " + ans);
		}
	}

}