import java.util.*;
public class Main {
    public static void main(String[] args){
        int[] arr = {20,30,40};
        int[] nuevo = new int[arr.length+1];
        nuevo[0]=10;
        System.arraycopy(arr,0,nuevo,1,arr.length);
        System.out.println(Arrays.toString(nuevo));
    }
}