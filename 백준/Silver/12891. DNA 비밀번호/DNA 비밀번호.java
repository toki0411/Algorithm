import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int s, p;
	static String str;
	static int A,C,G,T;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		s = Integer.parseInt(st.nextToken());
		p = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		str = st.nextToken();
		st = new StringTokenizer(br.readLine());
		A = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		G = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		
		System.out.println(makePassword());
	}
	private static int makePassword() {
		int cnt = 0;
		//문자열 기본 생성 
		
		for (int i = 0; i<p; i++) {
			char k = str.charAt(i);
			
			if (k == 'A' ) {
				A--;
			}
			else if (k == 'C' ) {
				C--;
			}
			else if (k == 'G' ) {
				G--;
			}
			else if (k == 'T' ) {
				T--;
			}		
		}
		if (A <= 0 && G <= 0 && C <= 0 && T <= 0) {
			cnt ++;
		}
		
		for (int i = 0; i<s-p; i++) {
			//맨앞에꺼 빼고
			if (str.charAt(i) == 'A') {
				A++;
			}else if (str.charAt(i) == 'C') {
				C++;
			}else if (str.charAt(i) == 'G') {
				G++;
			}else if (str.charAt(i) == 'T') {
				T++;
			}
			//한 개 추가 
			char k = str.charAt(p+i);
			if (k == 'A' ) {
				A--;
			}
			else if (k == 'C' ) {
				C--;
			}
			else if (k == 'G' ) {
				G--;
			}
			else if (k == 'T' ) {
				T--;
			}	
			if (A <= 0 && G <= 0 && C <= 0 && T <= 0) {
				cnt ++;
			}
		}
		return cnt;
	}
}