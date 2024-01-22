
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int arr [] = new int [8];
		for (int i = 0; i<8; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		boolean check = false;
		if (arr[0] == 1) {
			int idx = 1;
			for (int i = 0 ;i < 8; i++) {
				if (arr[i] != idx) {
					check = true;
					System.out.println("mixed");
					break;
				}
				idx ++;
			}
			if (!check) {
				System.out.println("ascending");
			}
		}
		else if (arr[0] == 8) {
			int idx = 8;
			for (int i = 0 ;i < 8; i++) {
				if (arr[i] != idx) {
					check = true;
					System.out.println("mixed");
					break;
				}
				idx --;
			}
			if (!check) {
				System.out.println("descending");
			}
		}
		else {
			System.out.println("mixed");
		}
		
		
    }
}