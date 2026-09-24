using System.Linq;
int[] arr = {10,20,30,40,50};
int indice=2;
arr = arr.Where((x,i)=>i!=indice).ToArray();