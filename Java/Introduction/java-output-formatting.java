// Java's System.out.printf function can be used to print formatted output. 
// The purpose of this exercise is to test your understanding of formatting 
// output using printf.

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String s1=sc.next();
                int x=sc.nextInt(); 
                //Complete this line
                System.out.printf("%-15s%03d%n", s1, x); // Note the formatting
                // See http://www.homeandlearn.co.uk/java/java_formatted_strings.html 
                // for more on formatting
            }
            System.out.println("================================");

    }
}