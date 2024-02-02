//
//  Copyright (c) 2021 HyeJin Shin All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int num1[10001];
int num2[10001];
vector<int> v;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    string a, b;
    string ans,tmp;
    int sum =0;
    cin >> a >>b;
    if (a.size() < b.size()){  //더 긴 수를 a에 저장
        tmp = a;
        a = b;
        b = tmp;
    }
    for(int i=0;i<a.size();i++){
        num1[i+1]=a[i]-'0';
    }
    for(int i=0;i<b.size();i++){
        num2[i+1+(a.size()-b.size())]=b[i]-'0';
    }
    for(int i=a.size();i>0;i--){
        sum = num1[i]+num2[i];
        if(sum >= 10){
            num1[i-1]++;
            sum = sum - 10;
        }
        v.push_back(sum);
    }
    if (num1[0] != 0) cout << 1;
    for(int i=v.size()-1;i>=0;i--){
        cout<<v[i];
    }
    
    
}
