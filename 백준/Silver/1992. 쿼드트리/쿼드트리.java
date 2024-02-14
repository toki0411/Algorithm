import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int [][] graph;
    static String s;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int [N][N];
        s = "";
        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < N; j++) {
                graph[i][j] = row.charAt(j) - '0';
            }
        }
        recursion(0,0, N );
        System.out.println(s);
    }
    private static boolean check(int x, int y, int len) {  //모두 다 같은 색인지 체크
        int tmp = graph[x][y];
        for (int i = x; i < x + len; i ++) {
            for (int j = y; j < y + len ; j++) {
                if (graph[i][j] != tmp) {
                    return false;
                }
            }
        }
        return true;
    }
    private static void recursion(int x, int y, int len){
        boolean key = check(x, y, len);
        if (key) {
            s += Integer.toString(graph[x][y]);
            return;
        }
        else {
            int range = len / 2;
            if (x + range < N && y + range < N && x >=0 && y >= 0 && range >= 1 ) {
                s += '(';
                recursion(x, y, range);
                recursion(x, y+range, range);
                recursion(x+range, y, range);
                recursion(x+range, y+range, range);
                s += ')';
            }
        }
    }

}
