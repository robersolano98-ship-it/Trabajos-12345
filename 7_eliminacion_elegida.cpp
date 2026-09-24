#include <vector>
#include <iostream>
using namespace std;
int main() {
    vector<int> arr = {10, 20, 30, 40, 50};
    int indice = 2;
    arr.erase(arr.begin() + indice);
    for(int x: arr) cout << x << " ";
}