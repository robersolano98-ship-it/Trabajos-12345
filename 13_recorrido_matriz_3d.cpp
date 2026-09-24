#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector<vector<vector<int>>> cubo = {{{1,2},{3,4}},{{5,6},{7,8}}};
    for(int i=0; i<cubo.size(); i++)
        for(int j=0; j<cubo[i].size(); j++)
            for(int k=0; k<cubo[i][j].size(); k++)
                cout<<"cubo["<<i<<"]["<<j<<"]["<<k<<"]="<<cubo[i][j][k]<<endl;
}