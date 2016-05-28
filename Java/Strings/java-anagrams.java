import java.io.*;
import java.util.*;

public class Solution {

   static boolean isAnagram(String A, String B) {
      //Complete the function
       char[] aChars = A.toCharArray();
       char[] bChars = B.toCharArray();
       Arrays.sort(aChars);
       Arrays.sort(bChars);
       boolean result = Arrays.equals(aChars, bChars);
       return result;
   }
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        A = A.toLowerCase();
        String B=sc.next();
        B = B.toLowerCase();
        boolean ret=isAnagram(A,B);
        if(ret)System.out.println("Anagrams");
        else System.out.println("Not Anagrams");
        
    }
}