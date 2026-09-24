import java.util.*;
public class Main {
    public static void main(String[] args){
        int[] arr = {10,20,30};
        int[] nuevo = Arrays.copyOf(arr, arr.length+1);
        nuevo[arr.length]=40;
        System.out.println(Arrays.toString(nuevo));
    }
}