import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int ans = 0;
		while (true) {
			if (N <= 2)break;
			else if (N % 3 == 0 && N % 5 == 0) {
				ans ++;
				N -= 5;
			}
			else if (N % 5 == 0) {
				ans ++;
				N -= 5;
			}
			else if (N % 3 == 0) {
				ans ++;
				N -= 3;
			}
			else if (N >= 5) {
				ans ++;
				N -= 5;
			}
			else if (N >= 3) {
				ans ++;
				N -= 3;
			}
		}
		
		if (N == 0) {
			System.out.println(ans);
		}
		else {
			System.out.println(-1);
		}
		
	}

}