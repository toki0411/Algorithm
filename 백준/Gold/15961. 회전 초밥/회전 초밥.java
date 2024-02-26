import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int d = scanner.nextInt();
        int k = scanner.nextInt();
        int c = scanner.nextInt();
        int[] sushi = new int[n];
        for (int i = 0; i < n; i++) {
            sushi[i] = scanner.nextInt();
        }
        
        Set<Integer> s = new HashSet<>();
        int[] cnt = new int[d + 1];
        for (int i = 0; i < k; i++) {
            cnt[sushi[i]]++;
            if (!s.contains(sushi[i])) {
                s.add(sushi[i]);
            }
        }
        
        int start = 0;
        int end = k;
        int ans = s.size();
        for (int i = 0; i < n; i++) {
            if (end >= n) {
                end = 0;
            }
            cnt[sushi[start]]--;
            cnt[sushi[end]]++;
            if (cnt[sushi[start]] <= 0) {
                s.remove(sushi[start]);
            }
            if (!s.contains(sushi[end])) {
                s.add(sushi[end]);
            }
            if (s.contains(c)) {
                ans = Math.max(ans, s.size());
            } else {
                ans = Math.max(ans, s.size() + 1);
            }
            
            start++;
            end++;
        }
        
        System.out.println(ans);
    }
}