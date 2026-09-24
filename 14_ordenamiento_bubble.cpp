#include <iostream>
#include <vector>
using namespace std;
vector<int> bubbleSort(vector<int> arr){
    for(int i=0; i<arr.size(); i++)
        for(int j=0; j<arr.size()-i-1; j++)
            if(arr[j]>arr[j+1]) swap(arr[j], arr[j+1]);
    return arr;
}
int main(){
    vector<int> arr = {64,34,25,12,22,11,90};
    arr = bubbleSort(arr);
    for(int x: arr) cout << x << " ";
}