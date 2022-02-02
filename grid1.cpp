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
    freopen("grid1.inp","r",stdin);
    freopen("grid2.out","w",stdout);
    int T;
    int N, M;
    int t,s,k;
    
    cin >>T;
    while(T--){
        cin >>N>>M>>t>>s>>k;
        if(t==1){  //타입 1
            int d = (k-1)/M;
            if(s==1){
                if(d%2==0)cout<<k<<endl;
                else cout<<M*2*d+1-k+M<<endl;}
            else if(s==2) {
                if(d%2==1)cout<<k<<endl;
                else cout<<M*2*d+1-k+M<<endl;
            }
            else if(s==3){
                if(d%2==0)cout<<(M*N+1)-k<<endl;
                else cout<<(N*M+M)-2*(M*(d+1)-k)-k<<endl;
            }
            else if(s==4){
                if(d%2==1)cout<<(M*N+1)-k<<endl;
                else cout<<(N*M+M)-2*(M*(d+1)-k)-k<<endl;
            }
        }
        else if(t==2){
            int d = (k-1)/N;
            int f = (k-1)%N;
            if(s==1){
                if(d%2==0)cout<<d+1+f*M<<endl;
                else cout<<d+1+M*(N-(f+1))<<endl;
            }
            else if(s==2){
                if(d%2==0)cout<<M-d+f*M<<endl;
                else cout<<M-d+M*(N-(f+1))<<endl;
            }
            else if(s==3){
                if(d%2==1)cout<<M-d+f*M<<endl;
                else cout<<M-d+M*(N-(f+1))<<endl;
            }
            else if(s==4){
                if(d%2==1)cout<<d+1+f*M<<endl;
                else cout<<d+1+M*(N-(f+1))<<endl;
            }
        }
    }//while
}

