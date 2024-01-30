

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] result;  //순열 결과 배열 
	static boolean[] isSelected;
	static int n;
	static int m;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		result = new int[m];
		isSelected = new boolean[n+1];
		
		NandM(0);
	}
	private static void NandM(int cnt) {
		if (cnt == m) {
			for (int j=0; j<m; j++) {
				System.out.print(result[j]+" ");
			}
			System.out.println();
			return;
		}
		
		for (int i=1; i<=n; i++) {
			if (!isSelected[i]) {
				isSelected[i] = true;
				result[cnt] = i;
				NandM(cnt+1);
				isSelected[i] = false;
			}
		}
	}

}
