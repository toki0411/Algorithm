import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static int N, Q;

    static ArrayList<ArrayList<int[]>> graph = new ArrayList<>();
    static boolean visited[];
    static int ans;
    static void dfs (int start, int length, int before){
        if (graph.get(start).size() <= 0) return;
        for (int i = 0; i < graph.get(start).size(); i++){
            int [] connect = graph.get(start).get(i);
            int video = connect[0];
            int usado = connect[1];

            if (before == video) {
                continue;
            }
            if (length <= usado) ans++;
            if (length <= usado && graph.get(video).size() > 0) {
                dfs(video, length, start);
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N+1; i++){
            graph.add(new ArrayList<>());
        }
        visited = new boolean [N+1];


        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            graph.get(p).add(new int[] {q,r});
            graph.get(q).add(new int[] {p,r});
        }

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            ans = 0;
            dfs(v,k, 0);

            System.out.println(ans);
        }
    }
}
