import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;
class Puddle {
	int s;
	int e;
	public Puddle(int s, int e) {
		this.s = s;
		this.e = e;
	}
	@Override
	public String toString() {
		return "Puddle [s=" + s + ", e=" + e + "]";
	}
}
class StartFirstComparator implements Comparator<Puddle> {

	@Override
	public int compare(Puddle o1, Puddle o2) {
		return Integer.compare(o1.s, o2.s);
	}
	
}
public class Main {

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
		
    	int N = Integer.parseInt(st.nextToken());
    	int L = Integer.parseInt(st.nextToken());
    	ArrayList<Puddle> puddles = new ArrayList<>();
    	for (int i = 0; i< N; i++) {
    		st = new StringTokenizer(br.readLine());
    		int start = Integer.parseInt(st.nextToken());
    		int end = Integer.parseInt(st.nextToken());
    		puddles.add(new Puddle(start, end));
    	}	
    	
    	Collections.sort(puddles, new StartFirstComparator());
    	int index = 0;
    	int cnt = 0;
    	//3가지 경우. 전 물웅덩이까지 끝난 경우, 끝난 위치가 다음 물웅덩이 전인지, 위인지(겹침), 뒤인지(이미 덮힌 경우)
    	for (int i = 0 ; i < N ; i ++) {
    		Puddle puddle = puddles.get(i);
    		if (index <= puddle.s) {
    			int tmp = 0;
    			index = puddle.s;
    			if ((puddle.e - index) % L != 0) {
    				tmp += (puddle.e - index) / L + 1;
    			}
    			else {
    				tmp += (puddle.e - index) / L;
    			}
    			cnt += tmp;
    			index += tmp * L;
    		}
    		else if (index > puddle.e) {
    			
    		}
    		else if (index > puddle.s) {
    			int tmp = 0;
    			if ((puddle.e - index) % L != 0) {
    				tmp += (puddle.e - index) / L + 1;
    			}
    			else {
    				tmp += (puddle.e - index) / L;
    			}
    			cnt += tmp;
    			index += tmp * L;
    		}
    		
    	}
    	System.out.println(cnt);
    }
}