import java.util.*;
class Solution {
    static char [] str;
    static boolean [] visited;
    static char number[];
    static HashSet<Integer> set;
    static void DFS(int cnt, int limit, int n){
        if (cnt == limit) {
            isPrime(cnt) ;
            return;
        }
        for (int i = 0; i < n; i ++) {
            if (!visited[i]){
                visited[i] = true;
                number[cnt] = str[i];
                DFS(cnt + 1, limit, n);
                visited[i] = false;
            }
        }
    }
    static boolean isPrime(int cnt){
        StringBuilder sb = new StringBuilder();
        for (int i =0 ;i < cnt; i++){
            sb.append(number[i]);
        }
        int num = Integer.parseInt(sb.toString());
        if (num < 2) return false;
        for (int i = 2; i*i <= num; i++) {
            if (num % i == 0) return false;
        }
        set.add(num);
        return true;
    }
    public int solution(String numbers) throws Exception{
      
        str = numbers.toCharArray();
        set = new HashSet<>();
        for (int i = 1; i<= numbers.length(); i++){
            number = new char [numbers.length()];
            visited = new boolean[numbers.length()];
            DFS(0, i, numbers.length());
        }
        return set.size();
    }
}