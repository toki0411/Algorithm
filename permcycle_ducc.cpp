#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	vector<int> arr = { 0 };
	int a;
	int T;
	int w;
	cin >> T;
	while (T--) {
		cin >> w;
		for (int i = 0; i < w; i++) {
			cin >> a;
			arr.push_back(a);
		}
		int oc = 0;
		int tc = 0;
		for (int i = 1; i <= w; i++) {
			int idx = arr[i];
			if (arr[i] == i) {
				oc++;
			}
			else if (i==arr[idx]) {
				tc++;    //2번 카운트 될 거라 나중에 사용할 때 /2 필수 
			}
			else
		}
	}
}