using System;
class Program{
    static int Binaria(int[] arr, int val){
        Array.Sort(arr);
        int l=0,r=arr.Length-1;
        while(l<=r){
            int m=(l+r)/2;
            if(arr[m]==val) return m;
            else if(arr[m]<val) l=m+1;
            else r=m-1;
        }
        return -1;
    }
    static void Main(){ Console.WriteLine(Binaria(new int[]{10,20,30,40,50},40)); }
}