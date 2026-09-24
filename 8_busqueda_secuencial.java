public class Main {
    static int secuencial(int[] arr, int val){
        for(int i=0;i<arr.length;i++) if(arr[i]==val) return i;
        return -1;
    }
    public static void main(String[] args){
        System.out.println(secuencial(new int[]{10,20,30,40},30));
    }
}