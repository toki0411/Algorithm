import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;
import static java.lang.Math.max;

public class Main {

    static int N, ans;
    static int[] building;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());  //리스트의 점수 개수
        ans = 0;
        building = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            building[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            //왼쪽
            double leftMin = 1000000000; int  lCnt = 0;
            for (int j = i - 1; j >= 0; j--) {
                double inclination = (double)(building[i] - building[j]) / (i - j);
                if (inclination < leftMin || j == i-1) {
                    lCnt++;
                    leftMin = inclination;
                }
            }
            //오른쪽
            double rightMax = 0; int rCnt = 0;
            for (int j = i + 1; j < N; j++) {
                double inclination = (double)( building[j] - building[i] ) / (j - i);
                if (inclination > rightMax || j == i+1) {
                    rCnt ++;
                    rightMax = inclination;
                }
            }
            //System.out.println(i + " " + lCnt + " " + rCnt);
            ans = Math.max(ans, lCnt + rCnt);
        }
        System.out.println(ans);

    }
}