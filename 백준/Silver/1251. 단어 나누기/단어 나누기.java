import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;

public class Main {

    static String s;
    static String ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine();

        for (int i = 1; i < s.length(); i++) {
            for (int j = 1; i + j < s.length(); j++) {
                stringCheck(i, j, s.length() - i - j);
            }
        }

        System.out.println(ans);
    }
    private static void stringCheck(int a, int b, int c) {
        // 세 구간을 각각 뒤집어서 연결
        String part1 = new StringBuilder(s.substring(0, a)).reverse().toString();
        String part2 = new StringBuilder(s.substring(a, a + b)).reverse().toString();
        String part3 = new StringBuilder(s.substring(a + b)).reverse().toString();

        String candidate = part1 + part2 + part3;

        if (ans == null || candidate.compareTo(ans) < 0){
            ans = candidate;
        }
    }

}