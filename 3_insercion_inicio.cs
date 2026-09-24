using System.Linq;
int[] arr = {20,30,40};
arr = new int[]{10}.Concat(arr).ToArray();
Console.WriteLine(string.Join(",",arr));