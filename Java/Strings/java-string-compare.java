import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        String word = sc.next();
        int k = sc.nextInt();
        String max = word.substring(0,k);
        String min = word.substring(0,k);
        for(int i = 0; i <= word.length() - k; i++){
            if(word.substring(i, i+k).compareTo(min) < 0) {
                min = word.substring(i, i+k);
            }
            if(word.substring(i, i+k).compareTo(max) > 0) {
                max = word.substring(i, i+k);
            }
        }
        System.out.println(min);
        System.out.println(max);
    }
}