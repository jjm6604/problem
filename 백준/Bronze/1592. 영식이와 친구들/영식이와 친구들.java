
import java.util.Scanner;

public class Main {
	

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[] f = new int[n];
		int M = scan.nextInt();
		int L = scan.nextInt();
		int a = 0;
		f[0] = 1;
		int count = 0;
		while(true) {
			if(f[a] == M) break;
			
			if (f[a] % 2 == 1) {
				a += L;
				if(a >= n) {
					a -= n;
				}
				
			}else {
				a -= L;
				if(a< 0) {
					a += n;
				}
			}
			f[a]++;
			count++;
			
		}
		System.out.println(count);
		scan.close();
	}
}