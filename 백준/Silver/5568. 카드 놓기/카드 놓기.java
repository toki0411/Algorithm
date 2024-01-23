import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static HashSet<Integer> hset=new HashSet();;
    public static String arr[];
    public static int k;
    public static int n;
    public static boolean [] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n =Integer.parseInt(br.readLine());
        k =Integer.parseInt(br.readLine());
        arr = new String[n];
        for (int i = 0; i < n; i ++) {
            arr[i] = br.readLine();
        }
        String ans = "";
        visited = new boolean[n];
        backtracking(0, ans);
        System.out.println(hset.size());
    }
    public static void backtracking(int cnt, String str){
        if (cnt == k) {
            hset.add(Integer.parseInt(str));
            return;
        }
        for (int i = 0; i < n; i++) {
            if (!visited[i] && cnt < k) {
                str += arr[i];
                visited[i] = true;
                backtracking(cnt+1, str);
                str = str.substring(0, str.length() - arr[i].length());
                visited[i] = false;
            }
        }

    }
}