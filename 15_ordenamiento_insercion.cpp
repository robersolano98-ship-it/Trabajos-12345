#include <iostream>
#include <vector>
using namespace std;
vector<int> insertionSort(vector<int> arr){
    for(int i=1; i<arr.size(); i++){
        int key=arr[i], j=i-1;
        while(j>=0 && arr[j]>key){ arr[j+1]=arr[j]; j--; }
        arr[j+1]=key;
    }
    return arr;
}
int main(){
    vector<int> arr = {64,34,25,12,22,11,90};
    arr = insertionSort(arr);
    for(int x: arr) cout << x << " ";
}