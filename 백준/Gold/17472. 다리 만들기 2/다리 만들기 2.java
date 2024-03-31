import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;

public class Main {

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[][] graph;
    static int[][] visited;
    static ArrayList<ArrayList<int[]>> island;
    static ArrayList<int[]> edgeList;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] size = br.readLine().split(" ");
        n = Integer.parseInt(size[0]);
        m = Integer.parseInt(size[1]);

        graph = new int[n][m];
        visited = new int[n][m];
        island = new ArrayList<>();
        island.add(new ArrayList<>());
        edgeList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(row[j]);
            }
        }

        int cnt = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] == 0 && graph[i][j] == 1) {
                    ArrayList<int[]> idx = bfs(i, j, cnt);
                    island.add(idx);
                    cnt++;
                }
            }
        }

        for (int i = 1; i < island.size(); i++) {
            for (int j = i + 1; j < island.size(); j++) {
                widthBridgeCheck(i, j);
                heightBridgeCheck(i, j);
            }
        }

        int[] parents = new int[island.size() + 1];
        make(parents);
        Collections.sort(edgeList, (a, b) -> a[2] - b[2]);

        int connected = 0;
        int weight = 0;
        for (int[] edge : edgeList) {
            if (!union(parents, edge[0], edge[1])) {
                continue;
            }
            weight += edge[2];
            connected++;
            if (connected == island.size() - 2) {
                break;
            }
        }

        if (connected != island.size() - 2) {
            System.out.println(-1);
        } else if (weight == 0) {
            System.out.println(-1);
        } else {
            System.out.println(weight);
        }
    }

    static ArrayList<int[]> bfs(int x, int y, int cnt) {
        ArrayList<int[]> idx = new ArrayList<>();
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{x, y});
        visited[x][y] = cnt;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            idx.add(current);
            int cx = current[0];
            int cy = current[1];
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (graph[nx][ny] == 1 && visited[nx][ny] == 0) {
                    q.add(new int[]{nx, ny});
                    visited[nx][ny] = cnt;
                }
            }
        }
        return idx;
    }

    static void widthBridgeCheck(int i, int j) {
        int cost = 100000;
        for (int[] coordI : island.get(i)) {
            int ix = coordI[0];
            int iy = coordI[1];
            for (int[] coordJ : island.get(j)) {
                int jx = coordJ[0];
                int jy = coordJ[1];
                if (ix == jx) {
                    if (iy > jy) {
                        boolean key = true;
                        for (int r = jy + 1; r < iy; r++) {
                            if (graph[ix][r] == 1) {
                                key = false;
                                break;
                            }
                        }
                        if (key) {
                            int tmp = Math.abs(jy - iy) - 1;
                            if (tmp < 2) continue;
                            cost = Math.min(tmp, cost);
                        }
                    } else if (iy < jy) {
                        boolean key = true;
                        for (int r = iy + 1; r < jy; r++) {
                            if (graph[ix][r] == 1) {
                                key = false;
                                break;
                            }
                        }
                        if (key) {
                            int tmp = Math.abs(jy - iy) - 1;
                            if (tmp < 2) continue;
                            cost = Math.min(tmp, cost);
                        }
                    }
                }
            }
        }
        if (cost != 100000) {
            edgeList.add(new int[]{i, j, cost});
        }
    }

    static void heightBridgeCheck(int i, int j) {
        int cost = 100000;
        for (int[] coordI : island.get(i)) {
            int ix = coordI[0];
            int iy = coordI[1];
            for (int[] coordJ : island.get(j)) {
                int jx = coordJ[0];
                int jy = coordJ[1];
                if (iy == jy) {
                    if (ix > jx) {
                        boolean key = true;
                        for (int r = jx + 1; r < ix; r++) {
                            if (graph[r][iy] == 1) {
                                key = false;
                                break;
                            }
                        }
                        if (key) {
                            int tmp = Math.abs(jx - ix) - 1;
                            if (tmp < 2) continue;
                            cost = Math.min(tmp, cost);
                        }
                    } else if (ix < jx) {
                        boolean key = true;
                        for (int r = ix + 1; r < jx; r++) {
                            if (graph[r][iy] == 1) {
                                key = false;
                                break;
                            }
                        }
                        if (key) {
                            int tmp = Math.abs(jx - ix) - 1;
                            if (tmp < 2) continue;
                            cost = Math.min(tmp, cost);
                        }
                    }
                }
            }
        }
        if (cost != 100000) {
            edgeList.add(new int[]{i, j, cost});
        }
    }

    static void make(int[] parents) {
        for (int k = 0; k < island.size() + 1; k++) {
            parents[k] = k;
        }
    }

    static int findParents(int[] parents, int x) {
        if (x == parents[x]) return x;
        parents[x] = findParents(parents, parents[x]);
        return parents[x];
    }

    static boolean union(int[] parents, int aa, int bb) {
        int aRoot = findParents(parents, aa);
        int bRoot = findParents(parents, bb);
        if (aRoot == bRoot) {
            return false;
        }
        if (aRoot < bRoot) {
            parents[bRoot] = aRoot;
        } else {
            parents[aRoot] = bRoot;
        }
        return true;
    }
}