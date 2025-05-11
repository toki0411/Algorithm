import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;
import static java.lang.Math.max;

public class Main {

    static int N, M, ans;
    static HashSet<String> keyword;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());  //리스트의 점수 개수
        M = Integer.parseInt(st.nextToken());  //리스트의 점수 개수
        ans = 0;
        keyword = new HashSet<>();

        for (int i = 0; i < N; i++){
            keyword.add(br.readLine());
        }

        for (int i = 0; i < M; i++) {
            String [] tokens = br.readLine().split(",");
            for (String token:tokens) {
                keyword.remove(token);
            }
            System.out.println(keyword.size());
        }

    }
}