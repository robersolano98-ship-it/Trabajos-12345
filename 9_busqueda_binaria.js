function binaria(arr, val){
  arr.sort((a,b)=>a-b);
  let l=0, r=arr.length-1;
  while(l<=r){
    let m=Math.floor((l+r)/2);
    if(arr[m]==val) return m;
    arr[m]<val? l=m+1 : r=m-1;
  }
  return -1;
}
console.log(binaria([10,20,30,40,50], 40));