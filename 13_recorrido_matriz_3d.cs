int[,,] cubo = { { {1,2},{3,4} }, { {5,6},{7,8} } };
for(int i=0;i<cubo.GetLength(0);i++)
 for(int j=0;j<cubo.GetLength(1);j++)
  for(int k=0;k<cubo.GetLength(2);k++)
   Console.WriteLine($"cubo[{i},{j},{k}]={cubo[i,j,k]}");