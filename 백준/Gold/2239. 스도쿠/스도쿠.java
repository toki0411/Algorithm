import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[][] arr = new int[10][10];
    static int N;
    static List<Pair> p = new ArrayList<>();

    static class Pair {
        int first;
        int second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }

    static boolean check(Pair p) {
        int x = p.first;
        int y = p.second;
        for (int i = 0; i < 9; i++) {
            if (arr[x][i] == arr[x][y] && i != y) return false;
            if (arr[i][y] == arr[x][y] && i != x) return false;
        }

        int nx = x / 3 * 3;
        int ny = y / 3 * 3;
        for (int i = nx; i < nx + 3; i++) {
            for (int k = ny; k < ny + 3; k++) {
                if (arr[i][k] == arr[x][y] && i != x && k != y) return false;
            }
        }
        return true;
    }

    static void Sudoku(int num) {
        if (num == N) {
            for (int k = 0; k < 9; k++) {
                for (int i = 0; i < 9; i++) {
                    System.out.print(arr[k][i]);
                }
                System.out.println();
            }
            System.exit(0);
        }
        int x = p.get(num).first;
        int y = p.get(num).second;
        for (int i = 1; i <= 9; i++) {
            arr[x][y] = i;
            if (check(p.get(num))) {
                Sudoku(num + 1);
            }
            arr[x][y] = 0;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int k = 0; k < 9; k++) {
            String str = br.readLine();
            for (int i = 0; i < 9; i++) {
                arr[k][i] = str.charAt(i) - '0';
                if (arr[k][i] == 0) {
                    N++;
                    p.add(new Pair(k, i));
                }
            }
        }
        Sudoku(0);
    }
}