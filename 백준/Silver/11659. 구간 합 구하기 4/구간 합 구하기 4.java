import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int arr[] = new int[n+1];
		int cal[] = new int[n+1];
		int val = 0;
		st = new StringTokenizer(br.readLine());
		for (int i =1 ; i<=n;i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			val += arr[i];
			cal[i] = val;
		}
		
		for (int q = 0; q < m; q++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			System.out.println(cal[end] - cal[start-1]);
		}
		
	}

}

//5 4 3 2 1
//5 9 12 14 15
//
//