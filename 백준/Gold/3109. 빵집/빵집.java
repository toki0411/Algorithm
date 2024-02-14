import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int R, C;
    static int[] dx = {-1, 0, 1};
    static int[] dy = {1, 1, 1};
    static char[][] graph;
    static int cnt,ans;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] RC = br.readLine().split(" ");
        R = Integer.parseInt(RC[0]);
        C = Integer.parseInt(RC[1]);
        graph = new char[R][C];
        
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                graph[i][j] = line.charAt(j);
            }
        }
        
        for (int i = 0 ; i<R; i++) {
//        	if (graph[i][0] != '.')continue;
        	if (dfs(i, 0, 0)) ans ++;
        }
        System.out.println(ans);
    }
    
    private static boolean dfs(int x, int y, int cnt) {
//    	System.out.println(x + " " + y + " " + cnt + " " + ans);
    	graph[x][y] = (char) cnt;
    	if (y == C-1) {
    		return true;
    	}
    	
    	for (int i = 0; i < 3; i++) {
    		int nx = x + dx[i];
    		int ny = y + dy[i];
    		
    		if (0<=nx && nx < R && 0 <= ny && ny < C && graph[nx][ny] =='.') {
    			if (dfs(nx, ny, 0))return true;
    		}
    	}
    	return false;
    }
}