import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            int x=sc.nextInt();
            //Complete this code
            double y = sc.nextDouble();
            String s = sc.nextLine(); // This captures a next-line character \n
            s = sc.nextLine(); // This is the next line AFTER the next-line character

            System.out.println("String: "+s);
            System.out.println("Double: "+y);
            System.out.println("Int: "+x);
    }
}