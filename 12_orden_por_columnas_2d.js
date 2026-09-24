let mat = [[3,1,2],[9,5,6],[8,7,4]];
let filas=mat.length, cols=mat[0].length;
for(let c=0;c<cols;c++){
  let col = [];
  for(let r=0;r<filas;r++) col.push(mat[r][c]);
  col.sort((a,b)=>a-b);
  for(let r=0;r<filas;r++) mat[r][c]=col[r];
}
console.log(mat);