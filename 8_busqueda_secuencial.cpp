#include <iostream>
#include <vector>
using namespace std;
int busquedaSecuencial(vector<int> arr, int valor){
    for(int i=0; i<arr.size(); i++) if(arr[i]==valor) return i;
    return -1;
}
int main(){
    vector<int> arr = {10,20,30,40};
    cout << busquedaSecuencial(arr, 30);
}