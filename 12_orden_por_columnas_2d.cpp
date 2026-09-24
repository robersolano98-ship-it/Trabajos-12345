#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
int main(){
    vector<vector<int>> mat = {{3,1,2},{9,5,6},{8,7,4}};
    int filas=mat.size(), cols=mat[0].size();
    for(int c=0; c<cols; c++){
        vector<int> col;
        for(int r=0; r<filas; r++) col.push_back(mat[r][c]);
        sort(col.begin(), col.end());
        for(int r=0; r<filas; r++) mat[r][c]=col[r];
    }
    for(auto &f: mat){ for(int x:f) cout<<x<<" "; cout<<endl; }
}