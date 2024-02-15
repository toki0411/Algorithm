import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
    static int T, N;
    static ArrayList<int[]> coordinates;
    static int mindis;
    static boolean visited[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            coordinates = new ArrayList<>();
            visited = new boolean[N+2];
            mindis = 100000000;
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N+2; i++) {
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                coordinates.add(new int[]{x, y});
            }
         
            visited[0] = true;
            dfs(coordinates.get(0)[0], coordinates.get(0)[1], 0, 0);
            System.out.println("#" + tc + " " +mindis);
        }
    }
    
    private static void dfs(int x, int y, int dis, int cnt) {
    	
    	if (dis > mindis) {
    		return;
    	}
    	if (cnt == N) {
    		dis += Math.abs(coordinates.get(1)[0]-x) + Math.abs(coordinates.get(1)[1]-y);
    		mindis = Math.min(dis, mindis);
    		return;
    	}
    	
    	for (int i = 2; i < coordinates.size(); i++) {
    		if (!visited[i]) {
    			visited[i] = true;
    			int val = Math.abs(coordinates.get(i)[0]-x) + Math.abs(coordinates.get(i)[1]-y);
    			dfs(coordinates.get(i)[0], coordinates.get(i)[1], dis + val, cnt + 1);
    			visited[i] = false;
    		}
    	}
    	
    }
}