import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int num[][]; 
	static boolean flag;

	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for (int t = 0; t < 4; t ++) {
			num = new int[6][3];
			int sum = 0;
			st= new StringTokenizer(br.readLine());
			for (int i = 0; i < 6; i++) {
				for (int j = 0; j < 3; j ++) {
					num[i][j] = Integer.parseInt(st.nextToken());
					sum += num[i][j];
				}
			}
			if (sum != 30) {
				System.out.print(0 + " ");
				continue;
			}
			flag = false;
			dfs(0,1);
			if(flag)System.out.print(1 + " ");
			else System.out.print(0 + " ");
		}

	}
	
	private static void dfs(int nowTeam, int nextTeam) {
		if (flag) return;
		
		if (nextTeam == 6) {
			nowTeam ++;
			nextTeam = nowTeam + 1;
		}
		
		if (nowTeam == 5) {
			flag = true;
			return;
		}
		
		//nowTeam승리
		if (num[nowTeam][0] > 0 && num[nextTeam][2] > 0) {
			num[nowTeam][0]--;
			num[nextTeam][2]--;
			dfs(nowTeam, nextTeam + 1);
			num[nowTeam][0]++;
			num[nextTeam][2]++;
		}
		//nowTeam무승부
		if (num[nowTeam][1] > 0 && num[nextTeam][1] > 0) {
			num[nowTeam][1]--;
			num[nextTeam][1]--;
			dfs(nowTeam, nextTeam + 1);
			num[nowTeam][1]++;
			num[nextTeam][1]++;
		}
		//nowTeam패배
		if (num[nowTeam][2] > 0 && num[nextTeam][0] > 0) {
			num[nowTeam][2]--;
			num[nextTeam][0]--;
			dfs(nowTeam, nextTeam + 1);
			num[nowTeam][2]++;
			num[nextTeam][0]++;
		}
	}

}