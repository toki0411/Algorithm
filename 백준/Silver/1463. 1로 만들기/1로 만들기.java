import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int dp[];
	static int X;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		X = Integer.parseInt(st.nextToken());
		
		dp = new int [1000001];
		dp[1] = 0;
		dp[2] = 1;
		dp[3] = 1;
		for (int i = 4; i <= X; i++) {
			dp[i] = i;
			if (i % 3 == 0) {
				dp[i] = Math.min(dp[i / 3]+1, dp[i]);
			}
			if (i % 2 == 0) {
				dp[i] = Math.min(dp[i / 2]+1, dp[i]);
			}
			
			dp[i] = Math.min(dp[i-1]+1, dp[i]);
			
		}
		System.out.println(dp[X]);
	}

}