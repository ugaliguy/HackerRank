import java.math.BigDecimal;
import java.util.*;
class Solution{

    public static void main(String []argh)
    {
        //Input
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] s = new String[n];
        for(int i=0;i<n;i++)
        {
            s[i]=sc.next();
        }

        //Write your code here
        Arrays.sort(s, new Comparator<String>() {
            public int compare(String first, String second) {
                BigDecimal bdFirst = new BigDecimal(first);
                BigDecimal bdSecond = new BigDecimal(second);
                int res = first.compareTo(second);
                return (res == 0) ? res : bdSecond.compareTo(bdFirst);
            }
        });
      
        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }

    }


}