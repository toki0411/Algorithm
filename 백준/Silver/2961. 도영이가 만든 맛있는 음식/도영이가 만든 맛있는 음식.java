import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int [] sour, bitter;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		sour = new int [n];
		bitter = new int [n];
		for (int i = 0 ; i< n; i++) {
			st = new StringTokenizer(br.readLine());
			sour[i] = Integer.parseInt(st.nextToken());
			bitter[i] = Integer.parseInt(st.nextToken());
		}
		
		System.out.println(subset(n));
	}
	private static int subset(int n) {
		int cnt= 1 << n;  // 1<<n : 2^n 부분집합의 개수 
		int sour_v = 0; int bitter_v = 0;
		int ans = Math.abs(sour[0]- bitter[0]);
		boolean key = false;
		for (int i =0; i<cnt; ++i) {
			sour_v = 1; bitter_v = 0; key = false;
			for (int position = 0; position < n; ++position) {  //부분집합 하나마다 각 위치의 원소들이 부분집합에 
				// i의 이진표현 값에서 position 위치 값이 1인지 0인지 체크 
				if ((i & 1 << position) != 0) {
					key = true;
					sour_v = sour_v * sour[position];
					bitter_v += bitter[position];
				}
			}
			if (Math.abs(sour_v - bitter_v) < ans && key) {
				ans = Math.abs(sour_v - bitter_v);
			}
		}
		return ans;
	}

}