import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	static int R, C;
	static char[][] graph;
	static int dx [] = {0,0,-1,1};
	static int dy [] = {1,-1,0,0};
	static int ans;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        graph = new char[R][C];
        
        for (int i = 0; i < R; i++) {
        	String line = br.readLine();
        	for (int j = 0; j < line.length(); j++) {
        		graph[i][j] = line.charAt(j);
        	}
        }
        String s = "";
        s+=graph[0][0];
        dfs(0,0, s);
        System.out.println(ans);
        
	}

	private static void dfs(int x, int y, String s) {
		ans = Math.max(ans, s.length());

		for (int i = 0; i < 4; i ++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >=0 && ny >=0 && nx < R && ny < C) {		
				boolean flag = false;
				for (int k = 0; k < s.length(); k++) {
					char c = s.charAt(k);
					if (c == graph[nx][ny]) {
						flag = true;
						break;
						}
					}
				if (!flag) {
					dfs(nx,ny,s+graph[nx][ny]);
				}
			}
		}

	}

}