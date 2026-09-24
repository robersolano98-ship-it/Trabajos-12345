#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
int main(){
    vector<vector<int>> mat = {{3,1,2},{9,5,6}};
    for(auto &fila: mat) sort(fila.begin(), fila.end());
    for(auto &f: mat){ for(int x:f) cout<<x<<" "; cout<<endl; }
}