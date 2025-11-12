import java.util.Arrays;
import java.util.*;
class Solution {
    int answer = -1;
    public int solution(int[] mats, String[][] park) {
        int x = park.length;
        int y = park[0].length; 
        // System.out.println(x + " " + y);
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++){
                if (park[i][j].equals("-1")) {
                    seek(mats, park, x, y, i, j);
                }
            }
        }
        return answer;
    }
    public void seek(int[] mats, String[][] park, int x, int y, int nowX, int nowY){
        Integer[] sorted_mats = Arrays.stream(mats).boxed().toArray(Integer[]::new);
        Arrays.sort(sorted_mats, Collections.reverseOrder());
        for (int i = 0; i < mats.length; i ++) {
            int len = sorted_mats[i];
            boolean key = true;
            for (int r = nowX; r < nowX + len; r ++) {
                for (int c = nowY; c < nowY + len; c++) {
                    //범위 체크 
                    if (r >= x || c >= y){
                        key = false; 
                        break;
                    }
                    //알파벳인지 체크 
                    if (!park[r][c].equals("-1")) {
                        key = false; 
                        break;
                    }
                }
                if (!key) break;
            }
            if (key) {
                answer = Math.max(len, answer);
                //System.out.println(len);
                break;
            }
        }
    }
}