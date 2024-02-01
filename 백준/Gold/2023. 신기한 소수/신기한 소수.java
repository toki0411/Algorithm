import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n=Integer.parseInt(br.readLine());
		
		findPrimeNumber("");
	}
	private static void findPrimeNumber(String s) {
		if (s.length() == n) {
			System.out.println(s);
			return;
		}
		if (s=="") {
			for (int i = 2; i< 10; i++) {
				String tmp = s + i;
				if (isPrime(Integer.parseInt(tmp))) {  //소수인지 체크 
					findPrimeNumber(tmp); 
				}
			}	
		}
		else {
			for (int i = 1; i< 10; i++) {
				String tmp = s + i;
				if (isPrime(Integer.parseInt(tmp))) {  //소수인지 체크 
					findPrimeNumber(tmp); 
				}
			}	
		}
		
		
	}
	
	private static boolean isPrime(int num) {
		boolean key = true;
		for (int i = 2; i<= num / 2; i++) {
			if (num % i == 0) {
				key = false;
				break;
			}
		}
		return key;
		
	}

}