import java.util.*;
public class Main {
    static int[] bubble(int[] arr){
        for(int i=0;i<arr.length;i++)
            for(int j=0;j<arr.length-i-1;j++)
                if(arr[j]>arr[j+1]){ int t=arr[j]; arr[j]=arr[j+1]; arr[j+1]=t; }
        return arr;
    }
    public static void main(String[] args){
        System.out.println(Arrays.toString(bubble(new int[]{64,34,25,12,22,11,90})));
    }
}