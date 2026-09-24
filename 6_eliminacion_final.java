import java.util.*;
public class Main {
    public static void main(String[] args){
        int[] arr = {10,20,30,40};
        int[] nuevo = Arrays.copyOf(arr, arr.length-1);
        System.out.println(Arrays.toString(nuevo));
    }
}