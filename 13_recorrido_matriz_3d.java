public class Main {
    public static void main(String[] args){
        int[][][] cubo = {{{1,2},{3,4}},{{5,6},{7,8}}};
        for(int i=0;i<cubo.length;i++)
            for(int j=0;j<cubo[i].length;j++)
                for(int k=0;k<cubo[i][j].length;k++)
                    System.out.println("cubo["+i+"]["+j+"]["+k+"]="+cubo[i][j][k]);
    }
}