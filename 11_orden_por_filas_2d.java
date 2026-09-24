import java.util.*;
public class Main {
    public static void main(String[] args){
        int[][] mat = {{3,1,2},{9,5,6}};
        for(int[] fila: mat) Arrays.sort(fila);
        for(int[] f: mat) System.out.println(Arrays.toString(f));
    }
}