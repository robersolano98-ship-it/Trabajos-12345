import java.util.*;
public class Main {
    public static void main(String[] args){
        int[][] mat = {{3,1,2},{9,5,6},{8,7,4}};
        int filas=mat.length, cols=mat[0].length;
        for(int c=0;c<cols;c++){
            int[] col=new int[filas];
            for(int r=0;r<filas;r++) col[r]=mat[r][c];
            Arrays.sort(col);
            for(int r=0;r<filas;r++) mat[r][c]=col[r];
        }
    }
}