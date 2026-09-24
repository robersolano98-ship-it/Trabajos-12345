import java.util.*;
public class Main {
    public static void main(String[] args){
        int[] arr = {10,20,30,40,50};
        int indice=2;
        int[] nuevo = new int[arr.length-1];
        System.arraycopy(arr,0,nuevo,0,indice);
        System.arraycopy(arr,indice+1,nuevo,indice,arr.length-indice-1);
        System.out.println(Arrays.toString(nuevo));
    }
}