import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		String str = bf.readLine();
		
		int n = Integer.parseInt(bf.readLine());
		
		int[] a = new int[27];
		
		a[26] = n; 
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		
		for(int i=0; i<26; i++) {
			a[i] = Integer.parseInt(st.nextToken());
		}
		String arrays[] = str.split(" ");
		char c, d;
		for(int i=0; i<str.length()-1; i++) {
			c = str.charAt(i);
			d = str.charAt(i+1);
			if(c != d) {
				if(c >= 'A' && c <= 'Z') {
					a[c - 65]--;
				}else if(c >= 'a' && c <= 'z') {
					a[c - 97]--;
				}else if(c == ' ') {
					a[26]--;
				}
			}
			
			
		}
		c = str.charAt(str.length()-1);
		
		if(c >= 'A' && c <= 'Z') {
			a[c - 65]--;
		}else if(c >= 'a' && c <= 'z') {
			a[c - 97]--;
		}
		
//		키보드를 쓸 때 같은 문자가 연속으로 나오거나 빈칸이 연속으로 나오는 경우 영재는 자판을 꾹 눌러 한 번만 사용해서 키보드를 좀 더 효율적으로 쓸 수 있다. 
		
		String result = "";
		
		
		for(int j=0; j<arrays.length; j++) {
			if(arrays[j].length() > 0) {
				if(arrays[j].charAt(0)>=97) {
					result += (char)(arrays[j].charAt(0)-32);	
				}else {
					result += arrays[j].charAt(0);	
				}
			}	
		}
				
		
		for(int i=0; i<result.length()-1; i++) {
			c = result.charAt(i);
			d = str.charAt(i+1);
			if(c != d) {
				a[c - 65]--;
			}
		}
		c = result.charAt(result.length()-1);
		a[c-65]--;
		for(int i=0; i<27; i++) {
			if(a[i] < 0) {
				System.out.println(-1);
				break;
			}
			if(i == 26) {
				System.out.println(result);
			}
		}
	}
}
