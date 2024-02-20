import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int N;
	static char[][] map;
	static boolean[][] isVisited;
	static int[] dr = {0,0,1,-1};
	static int[] dc = {1,-1,0,0};
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		map = new char[N][N];
		
		for(int i = 0; i < N; i++) {
			String input = br.readLine();
			
			for(int j = 0; j < N; j++) {
				map[i][j] = input.charAt(j);
			}
		}
		
		int notBlindnessCnt = 0;
		isVisited = new boolean[N][N];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(!isVisited[i][j]) {
					bfs(i, j, map[i][j], false);
					notBlindnessCnt++;
				}
			}
		}
		
		
		int BlindnessCnt = 0;
		isVisited = new boolean[N][N];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(!isVisited[i][j]) {
					bfs(i, j, map[i][j], true);
					BlindnessCnt++;
				}
			}
		}
		
		System.out.println(notBlindnessCnt + " " + BlindnessCnt);
	}
	
	static void bfs(int row, int col, char color, boolean isBlindness) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {row, col});
		isVisited[row][col] = true;
		
		while(!queue.isEmpty()) {
			int[] curV = queue.poll();
			int curRow = curV[0];
			int curCol = curV[1];
			
			
			
			for(int i = 0; i < 4; i++) {
				int nextRow = curRow + dr[i];
				int nextCol = curCol + dc[i];
				
				if(nextRow < 0 || nextRow >= N || nextCol < 0 || nextCol >= N || isVisited[nextRow][nextCol]) {
					continue;
				}
				
				// 색맹이 아닌 경우
				if(!isBlindness) {
					if(map[nextRow][nextCol] != color) {
						continue;
					}
				}
				// 색맹인 경우
				else {
					if(color == 'R' || color == 'G') {
						if(map[nextRow][nextCol] == 'B') continue;
					}
					else {
						if(map[nextRow][nextCol] != color) continue;
					}
				}
				
				queue.add(new int[] {nextRow, nextCol});
				isVisited[nextRow][nextCol] = true;
				
				
				
			}
			
			
			
		}
		
	}
	
}