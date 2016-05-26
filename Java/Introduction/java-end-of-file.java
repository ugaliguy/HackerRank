import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int lineCount = 1;
        while(scan.hasNext()){
            String readLine = scan.nextLine();
            System.out.println(lineCount + " " + readLine);
            lineCount += 1;
        }
    }
}