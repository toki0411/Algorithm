#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int len = arr.size();
    for(int i=0;i<len;i++){
        if(arr[i]!=arr[i+1]){
             answer.push_back(arr[i]);
        }
    }
    if(answer.size()==0&&arr[len-1]==0){
        answer.push_back(0);
    }

    return answer;
}
