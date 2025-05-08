import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;
import static java.lang.Math.max;

public class Main {

    static String s;
    static int N, answer;
    static int alpha[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine();
        N = s.length();
        answer = 0;
        alpha = new int[27];
        for (int i = 0; i < N; i++) {
            alpha[s.charAt(i) - 'a'] ++;
        }
        dfs(0, ' ');

        System.out.println(answer);
    }

    public static void dfs(int cnt, char prev){
        if (cnt == N) {
            answer ++;
            return;
        }
        for (int i = 0; i < 27; i++) {
            if (alpha[i] > 0) {
                char c = (char)(i + 'a');
                if (prev !=  c) {
                    alpha[i]--;
                    dfs(cnt + 1, c);
                    alpha[i]++;
                }
            }
        }
    }


}