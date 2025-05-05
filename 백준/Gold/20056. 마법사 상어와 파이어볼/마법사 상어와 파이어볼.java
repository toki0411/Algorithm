import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M, K;

    static List<Fireball> fireballs;
    static List<Fireball>[][] graph;
    static int[] dx = new int[]{-1,-1,0,1,1,1,0,-1};
    static int[] dy = new int[]{0, 1, 1,1,0,-1,-1,-1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        graph = new ArrayList[N+1][N+1];
        fireballs = new LinkedList<>();

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            Fireball fireball = new Fireball(r,c,m,s,d);
            fireballs.add(fireball);
        }
        for (int t = 0; t < K; t++){
            move();
            for (int i = 1; i < N+1; i++){
                for (int j = 1; j < N+1; j++){
                    if (graph[i][j].size() >= 2){
                        divide(i,j, graph[i][j]);
                    }
                }
            }
            addFireballs();
        }
        int answer = 0;
        for(Fireball fireball:fireballs) {
            answer += fireball.mass;
        }
        System.out.println(answer);

    }
    static void addFireballs(){
        fireballs = new LinkedList<>();
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                if(graph[i][j].size() > 0){
                    for(Fireball b:graph[i][j]){
                        fireballs.add(b);
                    }
                }
            }
        }
    }
    static void move(){
        for (int i = 1; i < N+1; i++) {
            for (int j = 1; j < N+1; j++) {
                graph[i][j] = new ArrayList<>();
            }
        }
        for(Fireball fireball:fireballs){
            int nx = fireball.x + dx[fireball.dir]*(fireball.speed%N);
            int ny = fireball.y + dy[fireball.dir]*(fireball.speed%N);

            if (nx <= 0) nx += N;
            if (ny <= 0) ny += N;
            if (nx > N) nx -= N;
            if (ny > N) ny -= N;
            fireball.x = nx;
            fireball.y = ny;
            graph[nx][ny].add(fireball);
        }
    }
    static void divide(int x, int y, List<Fireball> fireballs){
        int mass = 0;
        int speed = 0;
        boolean isEven = true;
        boolean isOdd = true;
        //합치기
        for (Fireball fireball: fireballs){
            mass += fireball.mass;
            speed += fireball.speed;
            if (fireball.dir % 2 == 0){
                isEven = false;
            }
            else {
                isOdd = false;
            }
        }
        mass = mass / 5;
        speed = speed / fireballs.size();
        int [] directions = new int[]{0,2,4,6};

        if (!isEven && !isOdd){
            directions[0] = 1;
            directions[1] = 3;
            directions[2] = 5;
            directions[3] = 7;
        }
        graph[x][y] = new ArrayList<>();
        if (mass <= 0){
            return;
        }
        for (int i = 0; i < 4; i ++){
            Fireball newFireball = new Fireball(x, y, mass, speed, directions[i]);
            graph[x][y].add(newFireball);
        }

    }

    public static class Fireball {
        int x;
        int y;

        int mass;
        int speed;
        int dir;

        public Fireball(int x, int y, int mass, int speed, int dir) {
            this.x = x;
            this.y = y;
            this.mass = mass;
            this.speed = speed;
            this.dir = dir;
        }
    }
}