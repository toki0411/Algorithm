import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static double ans;
    static int[] parents;
    static Star[] starList;
    static Edge[] edgeList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        parents = new int[n + 1];
        edgeList = new Edge[n * (n - 1) / 2];
        starList = new Star[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            double a = Double.parseDouble(st.nextToken());
            double b = Double.parseDouble(st.nextToken());
            starList[i] = new Star(a, b);
        }
        int idx = 0;
        for (int i = 0; i < n; i++) {
            double star1_x = starList[i].x;
            double star1_y = starList[i].y;
            for (int j = i + 1; j < n; j++) {
                double star2_x = starList[j].x;
                double star2_y = starList[j].y;
                double weight = Math.sqrt(Math.pow(Math.abs(star1_x - star2_x), 2) + Math.pow(Math.abs(star1_y - star2_y), 2));
                edgeList[idx] = new Edge(i, j, weight);
                idx++;
            }
        }
        make();
        Arrays.sort(edgeList);
        int cnt = 0;
        for (Edge edge : edgeList) {
            if (!union(edge.from, edge.to)) continue;
            ans += edge.weight;
            if (++cnt == n - 1) {
                break;
            }
        }
        System.out.println(Math.round(ans * 100) / 100.0);
    }

    private static class Edge implements Comparable<Edge> {
        int from;
        int to;
        double weight;

        public Edge(int from, int to, double weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return (int) (this.weight - o.weight);
        }
    }

    private static class Star {
        double x;
        double y;

        public Star(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    private static boolean union(int a, int b) {
        int aRoot = findParents(a);
        int bRoot = findParents(b);
        if (aRoot == bRoot) return false;
        if (aRoot < bRoot) {
            parents[bRoot] = aRoot;
        } else if (aRoot > bRoot) {
            parents[aRoot] = bRoot;
        }
        return true;
    }

    private static int findParents(int a) {
        if (a == parents[a]) return a;
        parents[a] = findParents(parents[a]);
        return parents[a];
    }

    private static void make() {
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
    }
}
