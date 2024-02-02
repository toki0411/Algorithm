import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {
	static char[] arr;

	public static void main(String[] args) throws IOException {
		Stack<Character> s = new Stack<Character>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for (int tc = 1; tc <= 10; tc ++) {
			int ans = 1;
			int limit = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			arr = st.nextToken().toCharArray();
			
			for (int i = 0; i< limit; i++) {
				if (arr[i]=='(' || arr[i] == '{'||arr[i]=='[' || arr[i]=='<') {
					s.push(arr[i]);
				}
				else if (arr[i] == ')') {
					if (s.peek() == '(') {
						s.pop();
					}
					else {
						ans = 0;
						break;
					}
				}
				else if (arr[i] == '}') {
					if (s.peek() == '{') {
						s.pop();
					}
					else {
						ans = 0;
						break;
					}
				}
				else if (arr[i] == ']') {
					if (s.peek() == '[') {
						s.pop();
					}
					else {
						ans = 0;
						break;
					}
				}
				else if (arr[i] == '>') {
					if (s.peek() == '<') {
						s.pop();
					}
					else {
						ans = 0;
						break;
					}
				}
			}
			System.out.println("#" + tc + " " + ans);
		}
	}

}