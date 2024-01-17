
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        String s = sc.next();
        String t = sc.next();

        while (t.length() > 0) {
            if (t.equals(s)) {
                answer = 1;
                break;
            }
            
            if (t.charAt(t.length() - 1)=='A') {
                t = t.substring(0, t.length() - 1);
            }
            else if (t.charAt(t.length() - 1) == 'B') {
            	t = t.substring(0, t.length() - 1);
            	StringBuffer sb = new StringBuffer(t);
                t = sb.reverse().toString();
            }
            else{
                break;
            }
        }
        System.out.println(answer);
        sc.close();
    }
}