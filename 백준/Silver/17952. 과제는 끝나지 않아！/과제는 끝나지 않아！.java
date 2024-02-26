import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	private static class Job {
		int score;
		int time;
		public Job(int score, int time) {
			super();
			this.score = score;
			this.time = time;
		}
		@Override
		public String toString() {
			return "Job [score=" + score + ", time=" + time + "]";
		}
		
	}
	static int N;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int total = 0;
		LinkedList<Job> s = new LinkedList<>();
		for (int t = 1; t<= N; t++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			if (a == 0) {
				if (s.isEmpty()) continue;
				Job j = s.pollLast();
				if (j.time - 1 == 0) total += j.score;
				else {
					Job j2 = new Job(j.score, j.time - 1);
					s.add(j2);
				}
			}
			else if (a == 1) {
				int b = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				if (c-1==0)total += b;
				else {
					s.add(new Job(b,c-1));
				}
			}

		}
		System.out.println(total);
	}

}