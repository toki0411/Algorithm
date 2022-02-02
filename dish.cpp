//
//  Copyright (c) 2021 HyeJin Shin All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("dish.inp","r",stdin);
    freopen("dish.out","w",stdout);
    
    int T;
    int n;
    string s;
    cin>>T;
    while(T--){
        int cnt=10;
        cin >> n;
        cin>>s;
       
        for(int i=1;i<s.length();i++){
            if(s[i]=='('){
                if(s[i-1]=='('){cnt+=5;}
                else if(s[i-1]==')'){cnt+=10;}
            }
            else if(s[i]==')'){
                if(s[i-1]=='('){cnt+=10;}
                else if(s[i-1]==')'){cnt+=5;}
            }
        }
        cout<<cnt<<endl;
    }
}

