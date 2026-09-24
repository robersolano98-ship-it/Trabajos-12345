using System;
class Program{
    static int Secuencial(int[] arr, int val){
        for(int i=0; i<arr.Length; i++) if(arr[i]==val) return i;
        return -1;
    }
    static void Main(){
        Console.WriteLine(Secuencial(new int[]{10,20,30,40},30));
    }
}