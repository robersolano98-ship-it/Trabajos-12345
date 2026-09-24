import java.util.*;
public class Main {
    static int binaria(int[] arr, int val){
        Arrays.sort(arr);
        int l=0,r=arr.length-1;
        while(l<=r){
            int m=(l+r)/2;
            if(arr[m]==val) return m;
            else if(arr[m]<val) l=m+1;
            else r=m-1;
        }
        return -1;
    }
    public static void main(String[] args){
        System.out.println(binaria(new int[]{10,20,30,40,50},40));
    }
}