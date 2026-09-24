int[,] mat = {{1,2,3},{4,5,6},{7,8,9}};
for(int i=0; i<mat.GetLength(0); i++){
    for(int j=0; j<mat.GetLength(1); j++) Console.Write(mat[i,j]+" ");
    Console.WriteLine();
}