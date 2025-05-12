import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Long.sum;
import static java.lang.Math.max;

public class Main {

    static int N;
    static char[][] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());  //리스트의 점수 개수
        graph = new char[N][N];
        boolean head = false;
        int headX = 0, headY = 0;
        for (int i = 0; i < N; i++) {
            char [] tmp = br.readLine().toCharArray();
            for (int j = 0; j < N; j++) {
                if (!head && tmp[j] == '*') {
                    head = true;
                    headX = i; headY = j;
                }
                graph[i][j] = tmp[j];
            }
        }
        System.out.println((headX+2) + " " + (headY + 1) );
        StringBuilder sb = new StringBuilder();
        //왼쪽 팔
        int cnt = 0;
        for (int i = 0; i < headY; i++) {
            if (graph[headX + 1][i] == '*') {
                cnt ++;
            }
        }
        sb.append(cnt + " ");
        cnt = 0;
        //오른쪽 팔
        for (int i = headY + 1; i < N; i++) {
            if (graph[headX + 1][i] == '*') {
                cnt ++;
            }
        }
        sb.append(cnt + " ");
        //허리
        cnt = 0;
        for (int i = headX + 2; i < N; i++) {
            if (graph[i][headY] == '*') {
                cnt ++;
                headX = i;
            }
        }
        sb.append(cnt + " ");
        //왼쪽 다리
        cnt = 0;
        for (int i = headX + 1; i < N; i++) {
            if (graph[i][headY - 1] == '*') {
                cnt ++;
            }
        }
        sb.append(cnt + " ");
        //오른쪽 다리
        cnt = 0;
        for (int i = headX + 1; i < N; i++) {
            if (graph[i][headY + 1] == '*') {
                cnt ++;
            }
        }
        sb.append(cnt);



        System.out.println(sb.toString());



    }
}