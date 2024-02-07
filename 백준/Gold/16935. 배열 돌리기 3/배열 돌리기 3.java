import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N, M, R;
	static int [][] graph;
	static int tmp, limit;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		limit = Math.max(N, M);
		graph = new int[limit][limit];
		
		for (int i = 0; i< N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j< M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i<R; i++) {
			int cmd = Integer.parseInt(st.nextToken());
			switch (cmd){
				case 1: cmd1(); break;
				case 2: cmd2(); break;
				case 3: cmd3(); break;
				case 4: cmd4(); break;
				case 5: cmd5(); break;
				case 6: cmd6(); break;
			}
		}
		for (int i = 0; i< N; i++) {
			for (int j = 0; j< M; j++) {
				System.out.print(graph[i][j] + " ");
			}
			System.out.println();
		}
		
	}
	
	public static void cmd1() {  //상하 반전
		for (int i = 0; i < N / 2; i++) {
			for (int j = 0; j<M; j++) {
				tmp = graph[i][j];
				graph[i][j] = graph[N-i-1][j];
				graph[N-1-i][j] = tmp;
			}
		}
	}
	
	public static void cmd2() {  //좌우 반전
		for (int i = 0; i < M / 2; i++) {
			for (int j = 0; j<N; j++) {
				tmp = graph[j][i];
				graph[j][i] = graph[j][M - i - 1];
				graph[j][M - i - 1] = tmp;
			}
		}
	}
	
	public static void cmd3() {  //오른쪽 90도
		int graph2[][] = new int[N][M];
		for (int i = 0; i< N; i++) {
			for (int j =0 ; j < M; j++) {
				graph2[i][j] = graph[i][j];
			}
		}
		for (int i =0; i<N; i++ ) {
			int arr[] = graph2[i];
			for (int j = 0; j< arr.length; j++) {
				graph[j][N - i-1] = arr[j];
			}
		}
		int temp2 = N;
		N = M;
		M = temp2;

	}
	public static void cmd4() {  //왼쪽 90도
		int graph2[][] = new int[N][M];
		for (int i = 0; i< N; i++) {
			for (int j =0 ; j < M; j++) {
				graph2[i][j] = graph[i][j];
			}
		}
		for (int i =0; i<N; i++ ) {
			int arr[] = graph2[i];
			for (int j = 0; j< arr.length; j++) {
				graph[M-j-1][i] = arr[j];
			}
		}
		int temp2 = N;
		N = M;
		M = temp2;
	}
	
	public static void cmd5() {  //
		int arr1[][] = new int[N/2][M/2];
		int arr2[][] = new int[N/2][M/2];
		int arr3[][] = new int[N/2][M/2];
		int arr4[][] = new int[N/2][M/2];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (i < N/2 && j < M / 2) {
					arr1[i][j] = graph[i][j];
				}
				else if (i < N/2 && j >= M/2) {
					arr2[i][j-M/2] = graph[i][j];
				}
				else if (i >= N/2 && j < M /2) {
					arr3[i-N/2][j] = graph[i][j];

				}
				else if (i >= N / 2 && j >= M/2) {
					arr4[i-N/2][j-M/2] = graph[i][j];

				}
			}
		}
		
		for (int i = 0; i < N/2; i++) { 
			for (int j = 0; j<M/2; j++) {
				graph[i][j+M/2] = arr1[i][j]; 
				graph[i+N/2][j] = arr4[i][j]; 
				graph[i+N/2][j+M/2] = arr2[i][j]; 
				graph[i][j] = arr3[i][j]; 
			}
		}
		
	}
	public static void cmd6() {
		int arr1[][] = new int[N/2][M/2];
		int arr2[][] = new int[N/2][M/2];
		int arr3[][] = new int[N/2][M/2];
		int arr4[][] = new int[N/2][M/2];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (i < N/2 && j < M / 2) {
					arr1[i][j] = graph[i][j];
				}
				else if (i < N/2 && j >= M/2) {
					arr2[i][j-M/2] = graph[i][j];
				}
				else if (i >= N/2 && j < M /2) {
					arr3[i-N/2][j] = graph[i][j];

				}
				else if (i >= N / 2 && j >= M/2) {
					arr4[i-N/2][j-M/2] = graph[i][j];

				}
			}
		}
		
		for (int i = 0; i < N/2; i++) { 
			for (int j = 0; j<M/2; j++) {
				graph[i][j+M/2] = arr4[i][j]; 
				graph[i+N/2][j] = arr1[i][j]; 
				graph[i+N/2][j+M/2] = arr3[i][j]; //
				graph[i][j] = arr2[i][j]; //
			}
		}
		
	}

}