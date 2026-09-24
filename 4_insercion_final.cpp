#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> arr = {10, 20, 30};
    arr.push_back(40);
    for(int x: arr) cout << x << " ";
}