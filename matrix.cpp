//
//  Copyright (c) 2021 HyeJin Shin All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;
int arr[300][300];
vector <pair<int,int>> v;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("matrix.inp","r",stdin);
    freopen("matrix.out","w",stdout);
    int T;
    int N=0;
    cin >> T;
    while(T--){
        if(N!=0){  //N이 0이 아니면(배열에 값을 받은 적이 있다면) arr배열을 초기화 해준다.
            for(int i=0;i<N;i++){
                fill_n(arr[i], N, 0);
            }
        }
        cin >> N;
        for(int i=0;i<N;i++){
            for(int k=0;k<N;k++){
                cin >> arr[i][k];
                if(arr[i][k]!=1)v.push_back({i,k});
            }
        }
        bool flag = false;
        for(int p=0;p<v.size();p++){
            int a =v[p].first;
            int b = v[p].second;
            bool key = false;
            for(int i=0;i<N;i++){
                if(key){break;}
                for(int k=0;k<N;k++){
                    if(arr[a][i]+arr[k][b]==arr[a][b]){
                        key = true;
                    }
                }
            }
            if(!key){cout<<0<<'\n'; flag = false; break;}
            else{flag = true;}
        }
        if(flag)cout<<1<<'\n';
        v.clear();
    }
}

