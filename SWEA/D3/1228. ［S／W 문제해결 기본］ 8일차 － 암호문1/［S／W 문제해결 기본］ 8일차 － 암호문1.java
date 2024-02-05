import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 1; tc <= 10; tc++) {
            int n = Integer.parseInt(br.readLine());
            LinkedList<Integer> arr = new LinkedList<>();

            String[] numbers = br.readLine().split(" ");
            for (String number : numbers) {
                arr.add(Integer.parseInt(number));
            }

            int m = Integer.parseInt(br.readLine());
            String[] commands = br.readLine().split("I");

            for (int i = 1; i < commands.length; i++) {
                String[] cmd = commands[i].trim().split(" ");

                // 명령어가 유효한지 확인
                if (cmd.length >= 3) {
                    int pos = Integer.parseInt(cmd[0]);
                    int count = Integer.parseInt(cmd[1]);

                    // 배열에 값 추가
                    for (int j = 2; j < cmd.length; j++) {
                        arr.add(pos++, Integer.parseInt(cmd[j]));
                    }
                }
            }

            System.out.print("#" + tc + " ");
            for (int i = 0; i < 10; i++) {
                System.out.print(arr.get(i) + " ");
            }
            System.out.println();
        }
    }
}