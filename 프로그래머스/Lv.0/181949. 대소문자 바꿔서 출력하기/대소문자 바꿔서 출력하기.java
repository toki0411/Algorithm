import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String answer = "";
        for (int i =0 ;i<s.length();i++) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c)) {
                answer += Character.toLowerCase(c);
            }
            else {
                answer += Character.toUpperCase(c);
            }
        }
        System.out.println(answer);
        sc.close();
    }
}