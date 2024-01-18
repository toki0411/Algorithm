import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int N;
    public static int[][] grid;
    public static boolean[][] visited;

    public static Queue<Cloud> clouds = new LinkedList<>();
    public static int[] dx = {0, -1, -1, -1, 0, 1, 1, 1};
    public static int[] dy = {-1, -1, 0, 1, 1, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        grid = new int[N][N];
        visited = new boolean[N][N];

        for(int i=0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j< N; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        clouds.add(new Cloud(N-1, 0));
        clouds.add(new Cloud(N-1, 1));
        clouds.add(new Cloud(N-2, 0));
        clouds.add(new Cloud(N-2, 1));

        while (M -- >0){
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken());

            stepOneTwo(d, s);
            stepThreeFour();
            stepFive();

        }
        int answer = 0;
        for (int []i : grid){
            for (int j : i){
                answer += j;
            }
        }

        System.out.println(answer);

    }
    public static void stepOneTwo(int d, int s){
        for (Cloud cloud : clouds){
            cloud.x = (N + cloud.x + dx[d] * (s % N)) % N;
            cloud.y = (N +cloud.y + dy[d] * (s % N)) % N;

            grid[cloud.x][cloud.y] ++;
        }
    }

    public static void stepThreeFour() {
        while (!clouds.isEmpty()){
            Cloud cloud = clouds.poll();
            visited[cloud.x][cloud.y] = true;

            int cnt = 0;
            int dx2[] = {-1, 1, -1,1};
            int dy2[] = {-1, 1,1,-1};
            for (int k = 0; k < 4 ; k++){
                int nx2 = cloud.x + dx2[k];
                int ny2 = cloud.y + dy2[k];

                if (nx2 >= 0 && ny2 >= 0 && nx2 < N && ny2 < N){
                    if (grid[nx2][ny2] > 0){
                        cnt ++;
                    }
                }
                
            }
            grid[cloud.x][cloud.y] += cnt;
        }
    }

    public static void stepFive(){
        for (int i= 0; i< N; i++){
            for (int j=0; j<N; j++) {
                if (!visited[i][j] && grid[i][j] >=2){
                    clouds.add(new Cloud(i,j));
                    grid[i][j] -= 2;
                }
            }
        }
        visited = new boolean[N][N];  //구름 사라진 칸 초기화

    }
    public static class Cloud {
        int x;
        int y;

        public Cloud(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}
