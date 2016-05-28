import java.io.*;
import java.util.*;

public class Solution {

   static boolean isAnagram(String A, String B) {
      //Complete the function
       int[] count = new int[26]; //This counts occurrences of letters in A
       A = A.toLowerCase(); 
       B = B.toLowerCase();
       if (A.length() != B.length()) {
           return false;
       }

       // initialize count to 0.
       for (int i = 0; i < 26; i++) {
           count[i] = 0;
       }

       // count letter frequency in A
       for (int i = 0; i < A.length(); i++) {
           int k = A.charAt(i) - 'a';
           count[k]++;
       }

       // minus letter frequency in B
       for (int i = 0; i < B.length(); i++) {
           int k = B.charAt(i) - 'a';
           count[k]--;
           if (count[k] < 0) {
               return false;
           }
       }
       return true;   
   }
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        boolean ret=isAnagram(A,B);
        if(ret)System.out.println("Anagrams");
        else System.out.println("Not Anagrams");      
    }
}