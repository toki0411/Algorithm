import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;


public class Solution {
	static class Edge implements Comparable<Edge>{
		int from;
		int to;
		double weight;
		public Edge(int from, int to, double weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}
		@Override
		public int compareTo(Edge o) {
		    if (this.weight < o.weight) return -1;
		    else if (this.weight > o.weight) return 1;
		    else return 0;
		}

	}
	static int N, tc;
	static int x, y;
	static double rate;
	static LinkedList<Edge> edgeList;
	static int[] xList, yList;
	static int [] parents;
	static double weight;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		tc = Integer.parseInt(st.nextToken());
		for (int t = 1; t <= tc; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			
			xList = new int [N];
			yList = new int [N];
			
			st = new StringTokenizer(br.readLine());
			for (int i =0 ; i < N; i++) {
				x = Integer.parseInt(st.nextToken());
				xList[i] = x;
			}
			st = new StringTokenizer(br.readLine());
			for (int i =0 ; i < N; i++) {
				y = Integer.parseInt(st.nextToken());
				yList[i] = y;
			}
			st = new StringTokenizer(br.readLine());
			rate = Double.parseDouble(st.nextToken());
			
			edgeList = new LinkedList<>();
	
			for (int i = 0; i < N; i++) {
				for (int j = i+1; j < N; j++) {
					edgeList.add(new Edge(i, j, Math.sqrt(Math.pow((xList[i]-xList[j]),2) + Math.pow((yList[i]-yList[j]),2))));
				}
			}
			
			Collections.sort(edgeList);
			parents = new int[N+1];
			for (int i = 1; i < N+1; i++) {
				parents[i] = i;
			}
			
			weight = 0;
			int cnt = 0;
			for (Edge edge : edgeList ) {
				if (!union(edge.from, edge.to)) {
					continue;
				}
				weight += Math.pow(edge.weight,2);
				if (++cnt == N-1) {
					break;
				}
			}
			double ans = rate * weight;
			System.out.println("#" + t + " " + Math.round(ans));
		}
	}
	
	private static boolean union(int a, int b) {
		int aRoot = findParents(a);
		int bRoot = findParents(b);
		if (aRoot == bRoot) return false;
		
		if (aRoot < bRoot) {
			parents[bRoot] = aRoot;
		}
		else {
			parents[aRoot] = bRoot;
		}
		return true;
	}
	private static int findParents (int x) {
		if (x==parents[x])return x;
		parents[x] = findParents(parents[x]);
		return parents[x];
	}
	
	

}