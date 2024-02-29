import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

import java.util.*;

public class Main {
    static int[][] arr;
    static ArrayList<Integer> v;
    static int N;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        arr = new int[N][N];
        v = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            v.add(i);
        }
        Collections.sort(v);
        
        for (int i = 0; i < N; i++) {
            for (int k = 0; k < N; k++) {
                arr[i][k] = scanner.nextInt();
            }
        }

        int min = Integer.MAX_VALUE;
        do {
            int cnt = 0;
            boolean key = false;
            for (int i = 0; i < N - 1; i++) {
                int a = v.get(i);
                int b = v.get(i + 1);
                if (arr[a][b] == 0) {
                    key = true;
                    break;
                }
                cnt += arr[a][b];
            }
            if (!key) {
                int a = v.get(N - 1);
                int b = v.get(0);
                if (arr[a][b] == 0) continue;
                cnt += arr[a][b];
                min = Math.min(min, cnt);
            }
        } while (nextPermutation(v));
        
        System.out.println(min);
    }

    static boolean nextPermutation(ArrayList<Integer> list) {
        int i = list.size() - 1;
        while (i > 0 && list.get(i - 1) >= list.get(i)) {
            i--;
        }
        if (i <= 0) return false;

        int j = list.size() - 1;
        while (list.get(j) <= list.get(i - 1)) {
            j--;
        }

        int temp = list.get(i - 1);
        list.set(i - 1, list.get(j));
        list.set(j, temp);

        j = list.size() - 1;
        while (i < j) {
            temp = list.get(i);
            list.set(i, list.get(j));
            list.set(j, temp);
            i++;
            j--;
        }
        return true;
    }
}