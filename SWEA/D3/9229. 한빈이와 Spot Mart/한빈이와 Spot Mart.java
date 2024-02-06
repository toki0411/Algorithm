import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int t = 1; t <= TC; t++) {
			
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			int arr[] = new int [n];
			for (int i = 0; i<n;i++) {
				arr[i]=Integer.parseInt(st.nextToken());
			}
			Arrays.sort(arr);
			int left = 0;
			int right = arr.length-1;
			int ans = -1;
			while (right > left) {
				int val = arr[left] + arr[right];
				if (val > m) {
					right--;
				}else {
					left ++;
					ans = Math.max(val, ans);
				}
			}
			System.out.println("#"+ t + " " + ans);
			
		}
	}

}