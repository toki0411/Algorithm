import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		StringBuilder answer = new StringBuilder();
		answer.append('<');
		Queue<Integer> q = new LinkedList<>();
		for (int i = 1; i<= n; i++) {
			q.add(i);
		}
		int index = 1;
		while (!q.isEmpty()) {
			int x = q.poll();
			if (index == k) {
				index = 1;
				answer.append(x);
				if (q.isEmpty()) {
					answer.append('>');
				}
				else {
					answer.append(", ");
				}
			}
			else {
				index ++;
				q.add(x);
			}
		}
		System.out.println(answer.toString());
		
	}

}