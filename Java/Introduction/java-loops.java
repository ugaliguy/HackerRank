import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=1; i<=t; i++){
            list.add(sc.nextInt());
            list.add(sc.nextInt());
            list.add(sc.nextInt());
        }
        
        int x=0,y=1,z=2; 
        int term=0;
        for(int i=0; i<t; i++){
            int a = list.get(x);
            int b = list.get(y);
            int n = list.get(z);
            for(int j=0; j<n; j++){
                term=a;
                for(int k=0; k<=j; k++){
                    term=term+((int)Math.pow(2,k))*b;
                }
                System.out.print(term+" ");
            }
                x+=3;
                y+=3;
                z+=3;
                System.out.println();
        }
        
    }    
}