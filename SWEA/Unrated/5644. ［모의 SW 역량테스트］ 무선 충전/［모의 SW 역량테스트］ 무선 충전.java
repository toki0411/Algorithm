import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	static int T, M, A; //M 이동시간, A BC의 개수 
	static ArrayList<BatteryCharger> battery;
	static int[] userA;
	static int[] userB;
	static int curUserA_x, curUserB_x;
	static int curUserA_y, curUserB_y;
	static int ans;

	static int nx[] = {0,0,1,0,-1};
	static int ny[] = {0,-1,0,1,0};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            A = Integer.parseInt(st.nextToken());
            userA = new int[M+1];
            userB = new int[M+1];
            ans = 0;
            curUserB_x = 10; curUserB_y = 10;
            curUserA_x = 1; curUserA_y = 1;
            st = new StringTokenizer(br.readLine());
            for (int k = 1; k <= M; k++) {
            	userA[k] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int k = 1; k <= M; k++) {
            	userB[k] = Integer.parseInt(st.nextToken());
            }
            
            battery = new ArrayList<>();
            for (int i = 0; i < A; i++) {  //충전소 위치
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int p = Integer.parseInt(st.nextToken());
                BatteryCharger b = new BatteryCharger(x,y,c,p);
                battery.add(b);
            }
            
            for (int t = 0; t <= M; t++) {
            	charge(t);
//            	System.out.println("**" + t + " " + ans);
            }
            
            System.out.println("#" + tc + " " + ans);
         }  
	}
        


	private static void charge(int t) {
		curUserA_x = curUserA_x + nx[userA[t]];
		curUserB_x = curUserB_x + nx[userB[t]];
		curUserA_y = curUserA_y + ny[userA[t]];
		curUserB_y = curUserB_y + ny[userB[t]];

		ArrayList <int[]> Alist = new ArrayList<>();
		ArrayList <int[]> Blist = new ArrayList<>();
		boolean key1, key2= false;
		boolean key = false;
		for (int i = 0; i < A; i++) {
			BatteryCharger b = battery.get(i);
			int bx = b.x; int by = b.y; int coverage = b.coverage; int perfomance = b.perfomance;
			key1 = false; key2 = false;
			if ((Math.abs(curUserA_x - b.x) + Math.abs(curUserA_y - b.y)) <= coverage) {
				Alist.add(new int[] {i, perfomance});
				key1 = true;
			}
			if ((Math.abs(curUserB_x - b.x) + Math.abs(curUserB_y - b.y)) <= coverage) {
				Blist.add(new int[] {i, perfomance});
				key2 = true;
			}
			
			if (key1 && key2) {
				key = true;
			}
		}
		
		//최대값 구하기
		//겹치지 않을 경우 각각의 최대값을 구해서 더함 
		if (!key) {
			if (Alist.size() > 0) {
				int val = 0;
				for (int i = 0; i <Alist.size(); i++) {
					if (Alist.get(i)[1] > val) {
						val= Alist.get(i)[1];
					}
				}
				ans += val;
			}
			if (Blist.size() > 0) {
				int val = 0;
				for (int i = 0; i <Blist.size(); i++) {
					if (Blist.get(i)[1] > val) {
						val= Blist.get(i)[1];
					}
				}
				ans += val;
			}
			
		
		}
		else {//겹칠 경우 
//			System.out.println("------------------------------" + t);
			int val=0; int tmpVal = 0;
			int Aidx=0; int Aprice = 0;
			int Bidx=0; int Bprice = 0;
		
			for (int i = 0; i < Alist.size(); i++) {
				Aidx = Alist.get(i)[0];
				Aprice = Alist.get(i)[1];
				for (int j = 0; j <Blist.size(); j++) {
					tmpVal = 0;
					Bidx = Blist.get(j)[0];
					Bprice = Blist.get(j)[1];
					if (Aidx == Bidx) {
						tmpVal = Aprice ; 
					}
					else {
						tmpVal = Aprice;
						tmpVal += Bprice;
					}
					val = Math.max(tmpVal, val);
				}
				
			}
			ans += val;
		}
	}



	private static class BatteryCharger {
    	int x;
    	int y;
    	int coverage;
    	int perfomance;
		public BatteryCharger(int x, int y, int coverage, int perfomance) {
			super();
			this.x = x;
			this.y = y;
			this.coverage = coverage;
			this.perfomance = perfomance;
		}
    }

}