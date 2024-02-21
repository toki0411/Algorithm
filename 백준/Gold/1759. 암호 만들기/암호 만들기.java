import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int L, C;
	static char[] word;
	static boolean[] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		word = new char[C];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < C; i++) {
			word[i] = st.nextToken().charAt(0);
		}
	 
		Arrays.sort(word);
	
		visited = new boolean[C];
		char [] pw = new char[C];
		dfs(pw,0,0);
	}
	
	private static void dfs(char [] pw, int cnt, int start) {
		if (cnt == L) {
			int moeum =0; int jaeum = 0;
			for (int i = 0; i < L; i++) {
				if (pw[i] == 'i' || pw[i] == 'e'|| pw[i] == 'u'|| pw[i] == 'a'|| pw[i] == 'o') {
					moeum ++;
				}
				else {
					jaeum ++;
				}
			}
		
			if (moeum >=1 && jaeum >= 2) {
				for (int i = 0; i < L; i++) {
					System.out.print(pw[i]);
				}
				System.out.println();
			}
			return;
		}
		
		for (int i = start; i < C; i++) {
			if (!visited[i]) {
				visited[i] = true;
				pw[cnt] = word[i];
				dfs(pw, cnt+1, i+1);
				visited[i] = false;
			}
		}
	}

}