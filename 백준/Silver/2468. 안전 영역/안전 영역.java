import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int[][] MAP = new int[N][N];
		int max_v = 0;
		int result = 0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				MAP[i][j] = sc.nextInt();
				if(max_v < MAP[i][j]) {
					max_v = MAP[i][j];
				}
			}
		}
		int[] direct1 = {-1, 0, 1, 0};
		int[] direct2 = {0, 1, 0, -1};
		
		
		for(int i=0; i<=max_v; i++) {
			int[][] v = new int[N][N];
			for(int j=0; j<N; j++) {
				for(int k=0; k<N; k++) {
					if(MAP[j][k] <= i) {
						v[j][k] = 1;
					}
				}
			}
			int cnt = 0;
			for(int j=0; j<N; j++) {
				for(int k=0; k<N; k++) {
					Queue<int[]> q = new LinkedList<>();
					if(v[j][k] == 0) {
						v[j][k] = 1;
						q.add(new int[]{j, k});
						cnt++;
						while(q.size() > 0) {
							int[] d = q.poll();
							int dx = d[0];
							int dy = d[1];
							for(int l=0; l<4; l++) {
								int x = dx + direct1[l];
								int y = dy + direct2[l];
								if ((x >= 0 && x < N) && (y >= 0 && y < N)) {
									
									if(v[x][y] == 0) {
										v[x][y] = 1;
										q.add(new int[] {x, y});
									}
								}
							}
						}
					}
				}
			}
			if(result < cnt) {
				result = cnt;
			}
		}
		
		System.out.println(result);
		
	}

}
