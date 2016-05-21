// This problem will test your knowledge on "if-else" statements.

// Given an integer  as input, check the following:

// If  is odd, print "Weird".
// If  is even and, in between the range of 2 and 5(inclusive), print "Not Weird".
// If  is even and, in between the range of 6 and 20(inclusive), print "Weird".
// If  is even and , print "Not Weird". 

    import java.io.*;
    import java.util.*;
    import java.text.*;
    import java.math.*;
    import java.util.regex.*;

    public class Solution {

        public static void main(String[] args) {

            Scanner sc=new Scanner(System.in);
            int n=sc.nextInt();            
            String ans="";
            if(n%2==1){
              ans = "Weird";
            }
            else{
            
               //Complete the code
                if ((n == 2 || n == 4 || n > 20)){
                    ans = "Not Weird";
                }
                else {
                    ans = "Weird";
                } 
            }
            System.out.println(ans);
            
        }
    }