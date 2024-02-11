import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
	
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int m = scan.nextInt();
		
		int[] A = new int[n];
		for(int i=0; i<n; i++) {
			A[i] = i + 1;
		}
		
		for(int i=0; i<m; i++) {
			int a = scan.nextInt();
			int b = scan.nextInt();
			a -= 1;
			b -= 1;
			for(int j=0; j<=((b-a)/2); j++) {
				int blank = A[b-j];
				A[b-j] = A[a+j];
				A[a+j] = blank;
				
			}
			
		}
		for(int i=0; i<n; i++) {
			System.out.print(A[i] + " ");
		}
		
		
    }
}