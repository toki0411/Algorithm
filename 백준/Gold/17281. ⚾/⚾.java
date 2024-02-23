import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] score;
	static boolean[] visited;
	static int[] sequence;
	static int ans = -1;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		score = new int[N][9]; 
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 9; j++) {
				score[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		visited = new boolean[9];
		sequence = new int[9];
		sequence[3] = 0;  // 3번째에 0번 타자가 hit
		visited[3] = true;  //3번째는 정해짐.
		permutation(1);
		
		System.out.println(ans);
		
	}
	
	private static void permutation(int cnt) {
		if (cnt == 9) {
			int k = play(sequence);
			ans = Math.max(k, ans);
//			System.out.println(Arrays.toString(sequence) + " " + k);
			return;
		}
		for (int i = 0; i < 9; i++) {
			if (!visited[i]) {
				visited[i] = true;
				sequence[i] = cnt;
				permutation(cnt + 1);
				visited[i] = false;
			}
		}
	}

	private static int play(int[] sequence) {
//		System.out.println(Arrays.toString(sequence));
		int cnt;
		int idx = 0;
		int total = 0;
		for (int eng = 0; eng < N; eng++) {
			cnt = 0;
			int inningScore = 0;
			boolean[] base = new boolean[4];
			while (cnt < 3) {
				if (score[eng][sequence[idx]]==1) { //안타 
					if (base[3]) {
						inningScore ++;
						base[3] = false;
					}
					if (base[2]) {
						base[3] = true;
						base[2] = false;
					}
					if (base[1]) {
						base[2] = true;
						
					}
					base[1] = true;
				}
				else if (score[eng][sequence[idx]]==2) { //2루타
					if (base[3]) {
						inningScore ++;
						base[3] = false;
					}
					if (base[2]) {
						inningScore++;
						
					}
					if (base[1]) {
						base[3] = true;
						base[1] = false;
					}
					base[2] = true;
				}
				else if (score[eng][sequence[idx]]==3) { //3루타
					if (base[3]) {
						inningScore++;
						
					}
					if (base[2]) {
						inningScore++;
						base[2] = false;
					}
					if (base[1]) {
						inningScore++;;
						base[1] = false;
					}
					base[3] = true;
				}
				else if (score[eng][sequence[idx]]==4) { //홈런 
					if (base[3]) {
						inningScore ++;
						base[3] = false;
					}
					if (base[2]) {
						inningScore++;
						base[2] = false;
					}
					if (base[1]) {
						inningScore++;
						base[1] = false;
					}
					inningScore ++;
				}
				else if (score[eng][sequence[idx]]==0) { //아웃 
					cnt ++;
				}
				idx ++;
				if (idx >= 9) {
					idx = 0;
				}
			}
			total += inningScore;
		}
		
//		System.out.println(total + " " +Arrays.toString(sequence));
		return total;
	}

}