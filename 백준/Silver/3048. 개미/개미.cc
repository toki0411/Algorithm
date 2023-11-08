//
//  Copyright (c) 2021 HyeJin Shin All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
string s1, s2;
string s3;
vector<pair<char,int>>v;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N1, N2;
    int T;
    cin >> N1 >> N2;
    cin >> s1 >> s2;
    cin >> T;
    for(int i=s1.length()-1;i>=0;i--){
        v.push_back(pair<char,int>(s1[i],0));
    }
    for(int i=0;i<s2.length();i++){
        v.push_back(pair<char,int>(s2[i],1));
    }
    
    for (int i = 0; i <T; i++) {  //몇 초 (1초당 탐색 한 번)
        for(int k=0; k<v.size()-1; k++){
            if(v[k].second==0 && v[k+1].second==1){
                swap(v[k],v[k+1]);
                k++;
            }
        }
    }
    for(int i=0;i<v.size();i++){
        cout <<v[i].first;
    }
    cout<<'\n';

}
