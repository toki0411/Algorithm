import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	static int T, N;
	static Point[] conv;
	static Point home, festival;
	static boolean [] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());
        while (T>0) {
        	T--;
        	st = new StringTokenizer(br.readLine());
        	N = Integer.parseInt(st.nextToken());
        	
        	st = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	
        	home = new Point(a, b);
        	conv = new Point[N];
        	visited = new boolean[N];
        	
        	for (int i = 0; i < N; i++) {
        		st = new StringTokenizer(br.readLine());
        		a = Integer.parseInt(st.nextToken());
            	b = Integer.parseInt(st.nextToken());
            	Point c = new Point(a, b);
            	conv[i] = c;
        	}
        	
        	st = new StringTokenizer(br.readLine());
    		a = Integer.parseInt(st.nextToken());
        	b = Integer.parseInt(st.nextToken());
        	festival = new Point(a, b);
        	
        	if (bfs(home)) {
        		System.out.println("happy");
        	}else {
        		System.out.println("sad");
        	}
        }
	}
	
	private static boolean bfs(Point home) {
		LinkedList<Point> q = new LinkedList<>();
		q.add(new Point(home.x, home.y));
		while (!q.isEmpty()) {
			Point p = q.poll();
			int x = p.x;
			int y = p.y;
		
			if (Math.abs(x - festival.x) + Math.abs(y - festival.y) <= 1000) {
				return true;
			}
			
			//편의점까지 갈 수 있는지 체크 
			for (int i = 0 ; i < conv.length; i ++) {
				int nx = conv[i].x;
				int ny = conv[i].y;
				if (Math.abs(x - nx) + Math.abs(y - ny) <= 1000 && ! visited[i] ) {
					visited[i] = true;
					q.add(new Point(nx, ny));
				}
			}
		}
		return false;
	}
	
	

}