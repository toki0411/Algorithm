
import java.util.*;

class Solution {
    static int robotCnt;
    static int answer;
    static Queue<int []>[] way;
    public int solution(int[][] points, int[][] routes) {
        robotCnt = routes.length;
        way = new LinkedList[robotCnt];
        for (int i = 0; i < robotCnt; i++){
            way[i] = new LinkedList<>();
        }
        move(points, routes);
        crashCalculate();
        return answer;
    }

    public static void move(int[][] points, int[][] routes){
        for (int i = 0; i < robotCnt; i++){
            int []point = points[routes[i][0] - 1];
            int x = point[0];
            int y = point[1];
            way[i].add(new int[]{x, y});
            for (int j = 1; j < routes[0].length; j++){
                int []newPoint = points[routes[i][j]-1];
                int nx = newPoint[0];
                int ny = newPoint[1];

                int tx = nx - x;
                int ty = ny - y;
                while (tx != 0){
                    if (tx > 0){
                        tx --;
                        x++;
                    }
                    else {
                        tx ++;
                        x --;
                    }
                    way[i].add(new int[]{x,y});
                }
                while (ty != 0){
                    if (ty > 0){
                        ty --;
                        y++;
                    }
                    else {
                        ty ++;
                        y--;
                    }
                    way[i].add(new int[]{x,y});
                }
            }
        }
    }

    public static void crashCalculate(){
        int count = 0;
        while(count != robotCnt){
            count = 0;
            int [][] graph = new int[101][101];
            for (int i = 0; i < robotCnt; i++) {
                if(way[i].isEmpty()) {
                    count++;
                    continue;
                }
                int [] tmp = way[i].poll();
                graph[tmp[0]][tmp[1]] ++;
               
            }

            for (int x = 0; x < 101; x++){
                for (int y = 0; y < 101; y++){
                    if (graph[x][y] > 1) answer++;
                }
            }
        }


    }
}
