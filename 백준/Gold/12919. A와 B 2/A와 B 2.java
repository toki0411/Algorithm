import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;
import static java.lang.Math.max;

public class Main {

    static String S, T;

    static char[] arr;
    static boolean flag;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine();
        T = br.readLine();
        flag = false;
        dfs(S, T, T.length() - 1);
        if (flag) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    static void dfs(String s, String t, int lastIdx) {
        if (s.length() == t.length()) {
            if (s.equals(t)) {
                flag = true;
            }
            return;
        }

        if (t.charAt(lastIdx) == 'A') {
            dfs(s, t.substring(0, lastIdx), lastIdx - 1);
        }
        StringBuilder sb = new StringBuilder(t).reverse();
        if (sb.charAt(lastIdx) == 'B') {
            dfs(s, sb.substring(0, lastIdx), lastIdx - 1);
        }

    }
}