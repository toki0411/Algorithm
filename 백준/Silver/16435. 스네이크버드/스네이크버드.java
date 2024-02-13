import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, height;
	static int fruit [];
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		height = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		fruit = new int [N];
		for (int i = 0; i<N; i++) {
			fruit[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i< N; i++) {
			int tmp = height;
			for (int j = 0; j<N; j++) {
				
				if (fruit[j] <= height && fruit[j] != -1) {
					height ++;
					fruit[j] = -1;
				}
			}
			
			if (tmp == height) {
				break;
			}
		}
		
		System.out.println(height);
	}

}