
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
    static int dx[] = {0,-1,1,0,0};
    static int dy[] = {0,0,0,-1,1};
    static int dirChange [] = {0,2,1,4,3};
    static int T, N, M, K;
    static ArrayList<Germ> germList;
    static int total;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());  //셀의 개수
            M = Integer.parseInt(st.nextToken());  //격리 시간
            K = Integer.parseInt(st.nextToken());  //군집 입력 개수
            germList = new ArrayList<>();
            for (int i = 0; i < K; i++ ){
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int num = Integer.parseInt(st.nextToken());
                int dir = Integer.parseInt(st.nextToken());
                germList.add(new Germ(x, y, num, dir));
            }

            for (int k = 0; k < M; k++){  //M시간 동안 시뮬레이션
                for (int i = 0; i < germList.size(); i++) {  //미생물들을 이동시킴
                    Germ g = germList.get(i);
                    g.x = g.x + dx[g.dir];
                    g.y = g.y + dy[g.dir];
                    if (g.x == 0 || g.y == 0 || g.x == N-1 || g.y == N-1) {
                        g.num = g.num / 2;
                        g.dir = dirChange[g.dir];
                    }
                    if (g.num == 0){
                        germList.remove(i);
                        i--;
                    }
                }
                Collections.sort(germList);

                for (int i = 0; i < germList.size()-1; i++) {  //겹치는 경우 합침
                    Germ now = germList.get(i);
                    Germ next = germList.get(i+1);
                    if (now.x == next.x && now.y == next.y) {
                        now.num += next.num;
                        germList.remove(i+1);
                        i--;
                    }
                }
            }
            total = 0;
            for (int i = 0; i < germList.size(); i++) {
                total += germList.get(i).num;
            }

            System.out.println("#" + tc + " " + total);
        }
    }
    private static class Germ implements Comparable<Germ> {
        int x;
        int y;
        int num;
        int dir;

        public Germ(int x, int y, int num, int dir) {
            this.x = x;
            this.y = y;
            this.num = num;
            this.dir = dir;
        }

        @Override
        public int compareTo(Germ o) {
            int cmp = Integer.compare(this.x, o.x);
            if(cmp != 0 ) return cmp;

            cmp = Integer.compare(this.y, o.y);
            if (cmp != 0)return cmp;

            return Integer.compare(o.num, this.num);
        }
    }
}
