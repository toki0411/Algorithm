import java.util.*;
class Solution {
    static int answer;
    static boolean [] visited;
    static int n;
    static void DFS(String begin, String target, String[] words, int cnt){
        if (begin.equals(target)){
            answer = Math.min(answer, cnt);
            return;
        }
        
        for (int i = 0; i < n; i++) {
            if (!visited[i] && changeAble(begin, words[i])){
                visited[i] = true;
                DFS(words[i], target, words, cnt + 1);
                visited[i] = false;
            }
        }
    }
    static boolean changeAble(String begin, String target){
        char [] start = begin.toCharArray();
        char [] end = target.toCharArray();
        int cnt = 0;
        for (int i = 0; i < start.length; i++){
            if (start[i] != end[i]) cnt ++;
        }
        if (cnt == 1)
            return true;
        else 
            return false;
    }
    public int solution(String begin, String target, String[] words) {
        answer = 1000000000;
        n = words.length;
        visited = new boolean[n];
        DFS(begin, target, words, 0);
        
        if (answer == 1000000000) answer = 0;
        return answer;
    }
}