let cubo = [[[1,2],[3,4]], [[5,6],[7,8]]];
for(let i=0;i<cubo.length;i++)
 for(let j=0;j<cubo[i].length;j++)
  for(let k=0;k<cubo[i][j].length;k++)
   console.log(`cubo[${i}][${j}][${k}] = ${cubo[i][j][k]}`);