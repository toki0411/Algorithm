import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int T, n;
	static int[] num, dp;
	public static void main(String[] args) throws IOException  {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		T = Integer.parseInt(st.nextToken());
		for (int tc = 1; tc <= T; tc ++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			num = new int[n];
			dp = new int[n];
			for (int l = 0; l < n; l++) {
				num[l] = Integer.parseInt(st.nextToken());
			}
			int ans = 0;
			for (int i = 0; i < n; i++) {
				dp[i] = 1;
				for (int j = 0; j < i; j++) {
					if (num[i] > num[j]) {
						dp[i] = Math.max(dp[j] + 1, dp[i]);
					}
				}
				if (dp[i] > ans) {
					ans = dp[i];
				}
			}
			
			System.out.println("#" + tc + " " + ans);
			
		}
		
		
	}

}