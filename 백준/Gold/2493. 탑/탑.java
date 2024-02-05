import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;
class Top {
	int index;
	int height;
	public Top(int index, int height) {
		super();
		this.index = index;
		this.height = height;
	}
}
public class Main {
	static int N;
	static int stack[], tower[];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringBuilder answer = new StringBuilder();
		Stack<Top> s = new Stack<>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i<=N; i++) {
			int height = Integer.parseInt(st.nextToken());
			if (s.isEmpty()) {
				answer.append("0 ");
				s.push(new Top(i, height));
			}
			else {
				while (true) {
					if (s.isEmpty()) {
						answer.append("0 ");
						s.push(new Top(i, height));
						break;
					}
					Top top = s.peek();
					if (top.height > height) {
						answer.append(top.index+" ");
						s.push(new Top(i, height));
						break;
					}
					else {
						s.pop();
					}
				}
				
			}
		}
		System.out.println(answer.toString());
	}

}