import java.util.*;
public class Main {
    static int[] insertion(int[] arr){
        for(int i=1;i<arr.length;i++){
            int key=arr[i], j=i-1;
            while(j>=0 && arr[j]>key){ arr[j+1]=arr[j]; j--; }
            arr[j+1]=key;
        }
        return arr;
    }
    public static void main(String[] args){
        System.out.println(Arrays.toString(insertion(new int[]{64,34,25,12,22,11,90})));
    }
}