#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T,N;
	int a;
	cin >> T;
	while (T--) {
		vector<int> max_idx = {};
		vector<int> min_idx= {};
		vector<int> arr = {};
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> a;
			arr.push_back(a);
		}
		int max = arr[0];
		int min = arr[0];
		for (int i = 0; i < N; i++) {
			if (min >= arr[i]) { min = arr[i];  }//같을때도 해 줘야함
			if (max <= arr[i]) { max = arr[i]; 
			}
		}
		for (int i = 0; i < N; i++) {
			if(arr[i]==min)min_idx.push_back(i);
			if(arr[i]==max)max_idx.push_back(i);
		}
		
		int c = abs(min_idx[0] - max_idx[0]);
		for (int i = 0; i < min_idx.size(); i++) {
			for (int k = 0; k < max_idx.size(); k++) {
				if (c >= abs(min_idx[i] - max_idx[k])) {
					c = abs(min_idx[i] - max_idx[k]);
				}
			}
		}

		cout << c << endl;
		c = 0;
	}
}