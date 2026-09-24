import java.util.*;
public class Main {
    public static void main(String[] args){
        int[] arr = {10,20,30,40};
        int[] nuevo = new int[arr.length-1];
        System.arraycopy(arr,1,nuevo,0,arr.length-1);
        System.out.println(Arrays.toString(nuevo));
    }
}