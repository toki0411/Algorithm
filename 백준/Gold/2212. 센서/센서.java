import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        if (K >= N){
            System.out.println(0);
            return;
        }
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i< N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        ArrayList <Integer> distance = new ArrayList<>();
        for (int i = 0 ; i< N-1; i++){
            distance.add(arr[i+1] - arr[i]);
        }
        Collections.sort(distance);
        int ans = 0;
        for (int i = 0; i < N-K; i++){
            ans += distance.get(i);
        }
        System.out.println(ans);


    }
}