import java.util.LinkedList;
import java.util.Queue;
class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        Queue <Integer> q = new LinkedList<>();
        //q.offer(k);
        for (int i = 0; i < players.length; i++){
            int cnt = (players[i] / m ) - q.size();
            for (int l = 0; l < cnt; l++) {
                q.offer(k);
                answer ++ ;
            }
            //System.out.println(i + " " + cnt + " " + answer);
            int len = q.size();
            for (int j = 0; j < len; j++) {
                int x = q.poll();
                if (x > 1) {
                    q.offer(x - 1);
                }
            }
        }
        return answer;
    }
}