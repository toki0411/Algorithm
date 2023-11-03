//
//  Copyright (c) 2022 HyeJin Shin All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector<char> alpha;
vector<string> ans;
char arr[16];
int L,C;
bool check(int x) {  //유망성 체크(사전순)
    bool key = false;
    for(int i=0;i<x-1;i++){
        int a = int(arr[i]);
        int b = int(arr[i+1]);
        if(a>b){key = true;break;}
    }
    vector<char> s;
    for(int i=0;i<x;i++){
        s.push_back(arr[i]);
    }
    
    for(int i=0;i<x-1;i++){
        if(s[i]==s[i+1]){key=true;break;}
    }
    if(key)return false;
    return true;
}
void dfs(int x){
    if(x==L){ //하나의 경우의 수 충족
        int m_cnt=0; //모음 카운트
        int j_cnt=0; //자음 카운트
        for(int i=0;i<x;i++){
            if(arr[i]=='a'||arr[i]=='i'||arr[i]=='e'||arr[i]=='o'||arr[i]=='u'){
                m_cnt ++;
            }
        }
        j_cnt = x - m_cnt;
        if(m_cnt <1 ||j_cnt<2)return;
        
//        vector<char> s;
//        for(int i=0;i<x;i++){
//            s.push_back(arr[i]);
//        }
//
//        for(int i=0;i<x-1;i++){
//            if(s[i]==s[i+1])return;
//        }
        
        string str;
        for(int i=0;i<L;i++){
            str+=arr[i];
        }
        ans.push_back(str);
        return;  //이전 노드로 돌아감
    }
    else {
        for(int i=0;i<C;i++){
            arr[x]=alpha[i];
            if(check(x)){  //유망성을 체크한 뒤
                if(x+1 == L){
                    if(check(x+1))dfs(x+1);
                }
                else {
                    dfs(x+1); } //그 다음 행 탐색
            }
        }
    }
    return;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    char c;
    cin>>L>>C;
    for(int i=0;i<C;i++){
        cin >> c;
        alpha.push_back(c);
    }
    dfs(0);
    sort(ans.begin(),ans.end());
    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<'\n';
    }
}
