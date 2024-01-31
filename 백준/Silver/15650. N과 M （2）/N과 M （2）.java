import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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
		
		NandM2(0,1);
	}
	private static void NandM2(int cnt, int start) {
		if (cnt == m) {
			for (int j=0; j<m; j++) {
				System.out.print(result[j]+" ");
			}
			System.out.println();
			return;
		}
		
		for (int i=start; i<=n; i++) {
			result[cnt] = i;
			NandM2(cnt+1, i+1);
		}
	}

}