#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int busquedaBinaria(vector<int> arr, int valor){
    sort(arr.begin(), arr.end());
    int izq=0, der=arr.size()-1;
    while(izq<=der){
        int mid=(izq+der)/2;
        if(arr[mid]==valor) return mid;
        else if(arr[mid]<valor) izq=mid+1;
        else der=mid-1;
    }
    return -1;
}
int main(){
    vector<int> arr = {10,20,30,40,50};
    cout << busquedaBinaria(arr, 40);
}