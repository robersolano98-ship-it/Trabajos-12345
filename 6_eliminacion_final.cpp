#include <vector>
#include <iostream>
using namespace std;
int main() {
    vector<int> arr = {10, 20, 30, 40};
    arr.pop_back();
    for(int x: arr) cout << x << " ";
}