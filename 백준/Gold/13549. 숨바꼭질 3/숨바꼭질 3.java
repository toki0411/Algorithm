import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

import static java.lang.Long.sum;
import static java.lang.Math.abs;
import static java.lang.Math.max;

public class Main {

    static int N, K;

    static int visited[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        visited = new int [100001];

        for (int i = 0; i < 100001; i++) {
            visited[i] = -1;
        }
        visited[N] = 0;

        Queue<Integer> q = new LinkedList<>();
        q.add(N);
        while (!q.isEmpty()) {
            int nx = q.poll();
            if (nx == K) {
                break;
            }
            if (0<= nx * 2 && nx * 2 <=100000 && visited[nx*2] == -1){
                visited[nx*2] = visited[nx];
                q.offer(nx * 2);
            }
            if (0<= nx - 1 && nx - 1 <=100000 && visited[nx-1] == -1){
                visited[nx-1] = visited[nx] +1;
                q.offer(nx - 1);
            }
            if (0<= nx + 1 && nx + 1 <=100000 && visited[nx+1] == -1){
                visited[nx+1] = visited[nx]+1;
                q.offer(nx + 1);
            }
        }

        System.out.println(visited[K]);
    }

}
