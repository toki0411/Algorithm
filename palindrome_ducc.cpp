#include <iostream>
#include <vector>
#include<string>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N;
	bool flag = false;
	string str;
	cin >> N;
	cin.ignore();
	while(N--) {
		getline(cin, str);
		int len = str.length();
		for (int i = 0; i < len; i++)
			str[i] = toupper(str[i]); //소문자를 대문자로 교환
		for (int i = 0; i < len / 2;i++) {
			if (str[i] == str[len - i - 1])
				flag = false;
			else
			{
				flag = true; break;
			}

		}
		if (flag == false)cout << 1<<endl;
		else cout << 0<<endl;
		flag = false;
	}
}