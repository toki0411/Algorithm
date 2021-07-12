#include <iostream>
#include <vector>
#include<string>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N;
	cin >> N;
	string str;
	cin.ignore();
	int c = 0;
	while (N--) {
		vector<string> arr = {};
		vector<string> arri = {};
		cin >> str;
		arr.push_back(str);
		cin >> str;
		arri.push_back(str);
		
		sort(arr[0].begin(), arr[0].end());
		sort(arri[0].begin(), arri[0].end());

		arr[0].erase(unique(arr[0].begin(), arr[0].end()), arr[0].end());
		arri[0].erase(unique(arri[0].begin(), arri[0].end()), arri[0].end());
		int lenarr = arr[0].size();
		int lenarri = arri[0].size();

		for (int i = 0; i < lenarr; i++) {
			for (int q = 0; q < lenarri; q++) {
				if (arr[0][i] == arri[0][q])c++;
			}
		}
		cout << c<<endl;
		c = 0;
	}
}