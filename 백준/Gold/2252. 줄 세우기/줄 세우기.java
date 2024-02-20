import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		StringBuilder sb = new StringBuilder();
		int[] inCount = new int[N];  //진입차수 저장할 배열
		
		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();  //그래프 저장할 리스트
		for (int i = 0; i < N; i++) {
			graph.add(new ArrayList<Integer>());
		}
		for (int j = 0; j < M; j++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph.get(a-1).add(b-1); 
			inCount[b-1] ++;
		}

        //위상 정렬에 사용할 큐 
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < inCount.length; i++) {
        	if (inCount[i] == 0)
        		q.offer(i);
        }
        while (!q.isEmpty()) {
        	int nodeNo = q.poll();
        	sb.append((nodeNo+1) + " ");
        	ArrayList<Integer> list = graph.get(nodeNo);  //인접 노드 
        	
        	for (int i = 0; i < list.size(); i++) {
        		inCount[list.get(i)] --;
        		if (inCount[list.get(i)]==0)
        			q.offer(list.get(i));
        	}
        }
        System.out.println(sb);
	}

}