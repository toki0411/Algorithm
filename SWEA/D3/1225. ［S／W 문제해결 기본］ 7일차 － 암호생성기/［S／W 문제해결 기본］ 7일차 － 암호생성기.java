import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Solution {
	static int num;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for (int tc = 1; tc <= 10; tc ++) {
			br.readLine();
			st = new StringTokenizer(br.readLine());
			Queue<Integer> q = new LinkedList<>();
			
			for (int k = 0; k<8; k++) {
				q.add(Integer.parseInt(st.nextToken()));
			}
			
			int x = 0;
			num = 1;
			while (true) {
				x = q.poll();
				x -= num;
				if (x <= 0) {
					q.add(0);
					break;
				}
				else {
					num ++;
					if (num > 5)num = 1;
					q.add(x);
				}
			}
			System.out.print("#" + tc + " ");
			for (int k = 0; k<8; k++) { 
				System.out.print(q.poll() + " ");
			}
		}
	}

}