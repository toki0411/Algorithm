import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int ans;
    static int[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());


        graph = new int[n+1];
        for (int i = 0; i < n; i ++){
            st = new StringTokenizer(br.readLine());
            graph[i] = Integer.parseInt(st.nextToken());
        }

        visited = new boolean[n+1];
        int cnt = 0;
        int num = 0;
        boolean flag = false;
        while(true) {
            cnt ++;
            if (graph[num] == k) {
                break;
            }
            else if (visited[graph[num]]){
                flag = true;
                break;
            }
            else {
                visited[graph[num]] = true;
                num = graph[num];
            }
        }
        if (flag){
            System.out.println(-1);
        }
        else {
            System.out.println(cnt);
        }
    }

}