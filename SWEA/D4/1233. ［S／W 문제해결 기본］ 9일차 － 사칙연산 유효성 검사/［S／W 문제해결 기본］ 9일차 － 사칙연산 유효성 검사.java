import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	static int size;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for (int tc = 1; tc<=10; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			boolean flag = false;
			for (int k = 0; k<N; k++) {
				st = new StringTokenizer(br.readLine());
				int num = Integer.parseInt(st.nextToken());
				char value = st.nextToken().charAt(0);
				
				boolean isNumber = false;
				//value가 숫자인지, operator인지 체크
				if (value == '+' || value == '-' || value == '*' || value == '/') {
					isNumber = false;
				}
				else {
					isNumber = true;
				}
				
				//자식이 있는지 체크 
				boolean hasChild = false;
				while(st.hasMoreTokens()) {
					hasChild = true;
					st.nextToken();
				}
				
				if (isNumber && hasChild) {  //숫자이면서, 자식이 있으면 (리프노드가 아니면) -> 유효성x
					flag = true;
				}
				else if (!isNumber && !hasChild) {  //연산자이면서, 자식이 없으면(리프노드이면) -> 유효성x
					flag = true;
				}
	
			}
			if (!flag) {
				System.out.println("#" + tc + " " + 1);
			}else {
				System.out.println("#" + tc + " " + 0);
			}
		}
	}

}