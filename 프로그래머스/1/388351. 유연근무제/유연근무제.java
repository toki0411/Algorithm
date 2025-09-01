class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        for (int i = 0; i < schedules.length; i++) {
            int cnt = 0;
            for (int j = startday; j < startday + 7; j++) {
                if (j % 7 == 6 || j % 7 == 0 ) continue;
                
                int limit = schedules[i] + 10 ;
                int minute = limit - (limit / 100) * 100;
                if (minute >= 60) {
                    limit = ((limit / 100) + 1 ) * 100 + (minute - 60);
                }
                if (limit >= timelogs[i][j-startday]) cnt ++;
            }
            if (cnt == 5) {
                answer ++;
            }
        }
        return answer;
    }
}