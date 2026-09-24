function secuencial(arr, val){
  for(let i=0; i<arr.length; i++) if(arr[i]==val) return i;
  return -1;
}
console.log(secuencial([10,20,30,40], 30));