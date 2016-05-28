import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String word = sc.next();
        /* Enter your code here. Print output to STDOUT. */
        char[] wordArray = word.toCharArray();
        String reverseWord = "";
        int n = word.length();
        for(int i = 0; i < n; i++){
            reverseWord += word.charAt(n - 1 - i);
        }
        if(word.compareTo(reverseWord) == 0){
            System.out.println("Yes");}
        else {
            System.out.println("No");}
        
    }
}