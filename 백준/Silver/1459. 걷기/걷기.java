import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long y = sc.nextLong();
        long w = sc.nextLong();
        long s = sc.nextLong();
        long straight, cross, combination;

        // 평행이동
        straight = (x+y) * w;

        // 대각선으로만 이동 (두 좌표 합 짝수)
        if ((x+y) % 2 == 0){
            cross = Math.max(x,y) * s;
        }
        else{      // 대각선으로만 이동 (두 좌표 합 홀수)
            cross = (Math.max(x,y) - 1) * s + w;
        }
        // 대각선으로 두 좌표 중 작은 것 만큼만 가고, 나머지는 평행이동
        combination = Math.min(x,y) * s + Math.abs(x-y) * w;


        System.out.println(Math.min(Math.min(straight, cross), combination));
        sc.close();
        
    }
}
