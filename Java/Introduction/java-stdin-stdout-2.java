// Most of the problems on HackerRank require reading input from stdin (standard input) and 
// writing output to stdout (standard output).

// One way to read from stdin is by using the Scanner class and specifying 
// the InputStream as System.in. Alternatively, you can use the BufferedReader class.

// Lines of output can be written to stdout with the System.out.println function.

// For this exercise, you need to read inputs from stdin and print them to stdout.

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