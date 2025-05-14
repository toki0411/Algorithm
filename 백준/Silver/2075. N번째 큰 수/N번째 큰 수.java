import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

import static java.lang.Long.sum;
import static java.lang.Math.abs;
import static java.lang.Math.max;

public class Main {

    static int N;
    static PriorityQueue<Integer> pq;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                int x = Integer.parseInt(st.nextToken());
                if (pq.size() < N) {
                    pq.add(x);
                }
                else {
                    if (pq.peek() < x ){
                        pq.poll();
                        pq.add(x);
                    }
                }
            }
        }
        int x = pq.poll();
        System.out.println(x);
        
    }

}