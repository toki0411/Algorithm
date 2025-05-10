import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;
import static java.lang.Math.max;

public class Main {

    static int N, P, score;
    static int [] num;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());  //리스트의 점수 개수
        score = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());  //점수의 총 개수
        num = new int[P];
        if (N > 0) st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }
        if (N < P) {
            num[N] = score;
            sort(num);
            rank(num, score, N+1);
        }
        else if (score <= num[N-1]) {
            System.out.println(-1);
        }
        else {
            num[N-1] = score;
            sort(num);
            rank(num, score, N);
        }

    }
    static void rank(int[] num, int score, int len) {
        int rank = 1;
        int cnt = 0;
        int prev = num[0];
        if (prev == score) {
            System.out.println(1);
            return;
        }
        //System.out.println(num[N] + ", " +  len+", " +  score);
        for (int i = 1; i < len; i++) {
            if (prev == num[i]) {
                cnt++;
            }
            else {
                rank += (cnt + 1);
                cnt = 0;
            }
            if (num[i] == score) {
                System.out.println(rank);
                return;
            }
            prev = num[i];
        }

    }
    static void sort(int[] num) {
        Integer[] intArr = Arrays.stream(num).boxed().toArray(Integer[]::new);
        Arrays.sort(intArr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return b-a;
            }
        });
        // 정렬된 결과를 원래 배열로 복사
        for (int i = 0; i < num.length; i++) {
            num[i] = intArr[i];
        }
    }


}