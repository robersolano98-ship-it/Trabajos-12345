#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> arr = {20, 30, 40};
    arr.insert(arr.begin(), 10);
    for(int x: arr) cout << x << " ";
}