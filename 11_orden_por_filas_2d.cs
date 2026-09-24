int[,] mat = {{3,1,2},{9,5,6}};
for(int i=0; i<mat.GetLength(0); i++){
    int[] fila = new int[mat.GetLength(1)];
    for(int j=0;j<fila.Length;j++) fila[j]=mat[i,j];
    Array.Sort(fila);
    for(int j=0;j<fila.Length;j++) mat[i,j]=fila[j];
}