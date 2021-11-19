//
//  Copyright (c) 2021 HyeJin Shin All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;
struct st{
    string num;
    string fir, sec;
};
bool cmp(st a, st b){
    
    return stoi(a.num)<stoi(b.num);
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N;
    int max = -1;
    bool key = false;
    map<string,int> m;
    cin>>N;
    vector<st> v(N);
    vector<string> arr;
    for(int i=0;i<N;i++){
        cin >> v[i].num>>v[i].fir>>v[i].sec;
        int length = v[i].fir.length();
        if(length>max){
            //cout<<'*';
            max = v[i].fir.length();}
        
        m[v[i].sec]++;
        if(!key){
            if(m[v[i].sec]>=2){key = true;}
        }
        if(m[v[i].sec]>=2){
            arr.push_back(v[i].sec);}
    }
    max ++;
    sort(v.begin(),v.end(),cmp);
    for(int i=0;i<v.size();i++){
        cout<<v[i].num<<' '<<v[i].fir;
        int num_blank=max-v[i].fir.length();
        for(int k=0;k<num_blank;k++)cout<<' ';
        cout<<v[i].sec<<'\n';
    }
    if(key)cout<<endl;

        sort(arr.begin(),arr.end());
        arr.erase(unique(arr.begin(),arr.end()),arr.end());
        for(int i=0;i<arr.size();i++)cout<<arr[i]<<' '<<m[arr[i]]<<'\n';
    }



