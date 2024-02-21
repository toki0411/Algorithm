import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int T,N,M;
	static int [] parent;
	public static void main(String[] args) throws IOException {
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		T = Integer.parseInt(st.nextToken());
		
		for (int tc = 1; tc <= T; tc++) {
			
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			parent = new int[N+1];
			for (int i = 0; i < N+1; i++) {
				parent[i] = i;
			}
			System.out.print("#"+tc+" ");
			for (int c = 0; c < M ; c ++) {
				st = new StringTokenizer(br.readLine());
				int cmd = Integer.parseInt(st.nextToken());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				if (cmd == 0) {
					union(a, b);
				}
				else if (cmd == 1) {
					int aParent = findParent(a);
					int bParent = findParent(b);
					if (aParent == bParent) {
						System.out.print(1);
					}
					else {
						System.out.print(0);
					}
				}
			}
			System.out.println();
	
		}
	}
	private static void union(int a, int b) {
		int aParent = findParent(a);
		int bParent = findParent(b);
		if (aParent < bParent) {
			parent[bParent] = aParent;
		}
		else if (aParent > bParent) {
			parent[aParent] = bParent;
		}
		else {
			return;
		}
	}
	private static int findParent(int x) {
		if(parent[x] != x) {
			parent[x] = findParent(parent[x]);
		}
		return parent[x];
	}
}