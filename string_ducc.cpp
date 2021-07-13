#include <iostream>
#include <vector>
#include<string>
#include <algorithm>
using namespace std;
string ABC = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
string abc = { 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' };
int findbig(char c){
	for (int i = 0; i < 26; i++) {
		if (ABC[i] == c)
			return i;
	}
}
int findsmall(char c) {
	for (int i = 0; i < 26; i++) {
		if (abc[i] == c)
			return i;
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	string str;
	int a = 0, b = 0;
	cin >> T;
	cin.ignore();
	while (T--) {
		bool flag = false;
		getline(cin, str);
		char arr[1000] = {};
		int len = str.length();
		for (int i = 0; i < len; i++) {
			arr[i] = str[i];
			if (((str[i] >= 'A') && (str[i] <= 'Z')) || (str[i] >= 'a') && (str[i] <= 'z')) {
				if (flag == false)a = i;
				 b = i; flag = true;
				 if (b == len - 1)goto statement;
				 else continue;
			}
			
			else if (flag == true) {
				statement:	
				char ex = arr[b];
				for (int k = b; k >= a; k--) { //환형이동
					if (k == a) arr[k] = ex;
					else arr[k] = arr[k - 1];
				}
				for (int q = a; q <= b; q++) {  //소문자 대문자 변경 
					if ((arr[q] >= 'A') && (arr[q] <= 'Z')) {
						arr[q] = tolower(arr[q]);
					}
					else
						arr[q] = toupper(arr[q]);
				}
				for (int q = a; q <= b; q++) {
					if ((arr[q] >= 'A') && (arr[q] <= 'Z')) {
						int idx = findbig(arr[q]);
						arr[q] = ABC[idx + 1];
					}
					else{
						int idx = findsmall(arr[q]);
						arr[q] = abc[idx + 1];
					}
				}

				flag = false;
			}
			else  continue;

		}
		for(int k=0;k<len;k++)
			cout << arr[k];
		cout << endl;
	}
}