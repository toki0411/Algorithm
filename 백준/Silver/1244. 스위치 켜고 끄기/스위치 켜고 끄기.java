import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int switches[] = new int[t+1];
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 1; i <= t; i++) {
			switches[i] = Integer.parseInt(st.nextToken());
		}
		
		int student_num = Integer.parseInt(br.readLine());
		for (int l = 0; l < student_num; l++) {
			st = new StringTokenizer(br.readLine());
			int gender = Integer.parseInt(st.nextToken());
			int num = Integer.parseInt(st.nextToken());
			if (gender == 1) {  //남자 
				for(int i = 1; i <= t; i++) { 
					if (i % num == 0) {
						switches[i] = 1-switches[i];
					}
				}

				
			}
			else {  //여자 
				ArrayList<Integer> arr = new ArrayList<>();
				arr.add(num);
				for(int i = 1; i <= t; i++) {
					int left = num - i;
					int right = num + i;
					if (left > 0 && right <= t && switches[left]==switches[right]) {
						arr.add(left);
						arr.add(right);
					}
					else {
						break;
					}
				}
				
				for (int i=0; i<arr.size(); i++) {
					switches[arr.get(i)] = 1-switches[arr.get(i)];
				}
				
				
			}
			
		}
		int cnt = 0;
		for (int i=1; i<=t;i++) {
			System.out.print(switches[i] + " ");
			cnt +=1;
			if (cnt == 20) {
				System.out.println();
				cnt = 0;
			}
		}
		
	}

}