
import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		Queue queue = new LinkedList();
		
		int n = scan.nextInt();
		
		for(int i=1; i<=n; i++){
		    queue.add(i);
		}
		
		while(queue.size() != 1){
		    queue.poll();
		    queue.add(queue.poll());
		}
		System.out.println(queue.poll());
	}
}
