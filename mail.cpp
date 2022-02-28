//
//  Copyright (c) 2021 HyeJin Shin All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
string s;
char alphabet[9]={'A','B','C','D','E','F','G','H','X'};
string code[8]={"000000","001111","010011","011100","100110","101001","110101","111010"};
int check(string s){
    int arr[8]={0,};
    for(int i=0;i<8;i++){
        int cnt = 0;
        for(int k=0;k<6;k++){
            if(s[k]!=code[i][k]){
                cnt++;
            }
        }
        arr[i]=cnt;
    }
    int min = 1e9;
    int idx = 0;
    for(int i=0;i<8;i++){
        if(arr[i]<min){
            min = arr[i];
            idx = i;
        }
    }
    
    if(min <= 1){return idx;}
    else return 8;
    
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("mail.inp","r",stdin);
    freopen("mail.out","w",stdout);
    
    int T;
    int N;
    cin >> T;
    while(T--){
        cin >>N;
        cin >> s;
        for(int i=0;i<6*N;i+=6){
            string sub = s.substr(i, 6);
            int a =check(sub);
            cout<<alphabet[a];
        }
        cout<<'\n';
    }
}

