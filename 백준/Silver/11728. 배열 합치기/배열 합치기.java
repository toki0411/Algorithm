import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;
import static java.lang.Math.max;

public class Main {

    static int N, M;
    static int arr[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N+M];

        st = new StringTokenizer(br.readLine());
        for (int j = 0; j < N; j++) {
            arr[j] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int j = N; j < N+M; j++) {
            arr[j] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();

        for(int r : arr) {
            sb.append(r+" ");

        }
        System.out.println(sb);


    }
}