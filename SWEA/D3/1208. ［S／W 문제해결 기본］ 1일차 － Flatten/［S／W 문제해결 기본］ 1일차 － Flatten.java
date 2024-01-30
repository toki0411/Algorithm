
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		for (int tc = 1; tc <= 10; tc ++) {
		
			int dump = Integer.parseInt(br.readLine());
			
			int height[] = new int[101];
	
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int max = 1; int min = 100;
			for (int j = 0; j < 100; j++) {
				int k = Integer.parseInt(st.nextToken());
				height[k] += 1;
				if (k < min) {  //최솟값 찾기 
					min = k;
				}
				if (k > max) {  //최댓값 찾기 
					max = k;
				}
			}
			
			for (int i = 0; i < dump; i++) {
				if (Math.abs(max - min) <= 1 ) {
					break;
				}
				height[max] -= 1;
				height[max-1] += 1;
				height[min] -= 1;
				height[min+1] += 1;
				
				if (height[max] == 0) {  //최대값 갱신 
					for (int l=max; l > 0; l--) {
						if (height[l] > 0) {
							max = l;
							break;
						}
					}
				}
				if (height[min] == 0) {
					for (int l=min; l < 101; l++) {
						if (height[l] > 0) {
							min = l;
							break;
						}
					}
				}

			}
		

			System.out.println("#"+tc+" " + (max - min));
		}
		
	}

}
