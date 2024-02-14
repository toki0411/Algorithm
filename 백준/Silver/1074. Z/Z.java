import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int n,r,c;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        r = Integer.parseInt(inputs[1]);
        c = Integer.parseInt(inputs[2]);

        int limit = (int)Math.pow(2,n);
        zFind(0,0,limit, 0);
	}

	private static void zFind(int x, int y, int limit, int cnt) {
		if (limit == 2) {
			for (int i=x; i<=x+1; i++) {
                for (int j = y; j <= y + 1; j++) {
                    if (i == r && j == c) {
                        System.out.println(cnt);
                        return;
                    }
                    cnt++;
                }
			}
			return;
		}
		int range = limit / 2;

        if (x<=r && r<x+range && y<=c && c<y+range){
            zFind(x, y, range, cnt);
        } else if (x <= r && r < x + range && y + range <= c && c<y+limit){
            zFind(x, y+range, range, cnt + range * range);
        } else if (x+range <=r && r < x+limit && y <= c && c < y+range) {
            zFind(x + range, y, range, cnt + range * range * 2 );
        } else {
            zFind(x+range, y+range, range, cnt + range * range * 3 );
        }

	}
}