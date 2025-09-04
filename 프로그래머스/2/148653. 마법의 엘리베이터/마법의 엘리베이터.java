class Solution {
    public int solution(int storey) {
        int answer = 0;
        while (storey > 0) {
            int num = storey % 10;
            storey = storey / 10;
            if (num < 5) {
                answer += num ;
            }
            else if (num > 5) {
                answer += (10 - num) ;
                storey += 1;
            }
            else {
                int tmpNum = storey % 10;
                answer += 5;
                if (tmpNum >= 5) {
                    storey += 1;
                }
            }
        }
        return answer;
    }
}