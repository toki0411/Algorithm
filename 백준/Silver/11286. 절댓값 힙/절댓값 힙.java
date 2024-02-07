import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		PriorityQueue<Number> pq = new PriorityQueue<>();
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			if (x == 0) {
				if (pq.isEmpty()) System.out.println(0);
				else {
					Number ans = pq.poll();
					System.out.println(ans.num);
				}
			}
			else {
				pq.add(new Number(Math.abs(x), x));
			}
		}

	}
	static class Number implements Comparable <Number>{
		private int absNum;
		private int num;
		public Number(int absNum, int num) {
			super();
			this.absNum = absNum;
			this.num = num;
		}
		@Override
		public int compareTo(Number o) {
			int key = this.absNum - o.absNum;
			if (key == 0) {
				return this.num - o.num;
			}
			else {
				return this.absNum - o.absNum;
			}
		}
		
		
	}

}