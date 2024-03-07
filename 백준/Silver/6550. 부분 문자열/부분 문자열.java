import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {

		Scanner scan = new Scanner(System.in);
		
		while(scan.hasNext()) {
			String str = scan.next();
			String str2 = scan.next();
			
			String result = "No";
			
			int count = 0;
			int k = 0;
			for(int i=0; i<str.length(); i++) {
				
				for(int j=k; j<str2.length(); j++) {
					if(str.charAt(i) == str2.charAt(j)) {
						k = j+1;
						count++;
						break;
					}
				}
			}
			if(count == str.length()) {
				result = "Yes";
			}
			
			
			System.out.println(result);
		}
		scan.close();
	}
	
	
}

	