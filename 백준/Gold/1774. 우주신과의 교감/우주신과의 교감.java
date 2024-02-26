import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static Point[] nodeList;
    static Edge[] edgeList;
    static int parents[];
    static double weight;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nodeList = new Point[N+1];
        edgeList = new Edge[N * (N-1) / 2];
        parents = new int[N+1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            nodeList[i] = new Point(x, y);
        }
        int idx = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = i+1; j <= N; j++) {
                edgeList[idx] = new Edge(i, j, Math.sqrt(Math.pow(Math.abs(nodeList[i].x - nodeList[j].x) ,2) +
                        Math.pow(Math.abs(nodeList[i].y - nodeList[j].y),2)));
                idx ++;
            }
        }

        Arrays.sort(edgeList);
//		System.out.println(Arrays.toString(edgeList));
        for (int i = 1; i<=N; i++) {
            parents[i] = i;
        }
        int cnt = 0;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (union(a,b)) cnt ++;
        }
        for (Edge edge : edgeList) {
            if (!union(edge.from, edge.to)) {
                continue;
            }
            weight += edge.weight;
            if (++cnt == N-1) {
                break;
            }
        }
        System.out.printf("%.2f\n", weight);
    }

    private static boolean union(int a, int b) {
        int aRoot = findParents(a);
        int bRoot = findParents(b);
        if (aRoot == bRoot) return false;
        if (aRoot < bRoot) {
            parents[bRoot] = aRoot;
        }
        else if (aRoot > bRoot) {
            parents[aRoot] = bRoot;
        }
        return true;

    }
    private static int findParents(int a) {
        if (a == parents[a]) return a;
        parents[a] = findParents(parents[a]);
        return parents[a];
    }

    private static class Edge implements Comparable<Edge> {
        int from;
        int to;
        double weight;
        public Edge(int from, int to, double weight) {
            super();
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
        @Override
        public String toString() {
            return "Edge [from=" + from + ", to=" + to + ", weight=" + weight + "]";
        }
        @Override
        public int compareTo(Edge o) {
            double cmp = this.weight - o.weight;
            if (cmp <= 0)return -1;
            return 1;

        }


    }
}