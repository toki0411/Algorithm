import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;
import static java.lang.Math.max;

public class Main {

    static int N, X;
    static int[] num;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());  //리스트의 점수 개수
        X = Integer.parseInt(st.nextToken());

        num = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }
        int left = 0, cnt = 0;
        int sum = 0, max = -1;
        for (int i = 0; i < X - 1; i++) {
            sum += num[i];
        }
        for (int i = X - 1; i < N; i++) {
            sum += num[i];
            if (sum > max) {
                max = sum;
                cnt = 1;
            }
            else if (sum == max) {
                cnt ++;
            }
            sum -= num[left++];

        }
        if (max == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(max);
            System.out.println(cnt);
        }

    }


}