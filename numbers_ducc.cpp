#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N, a;
	int n;
	int q = 1;
	cin >> N;
	for(int q=0;q<N;q++) {
		vector<int> arr = { };
		cin >> a;
		for (int i = 0; i < a; i++) {
			cin >> n;
			arr.push_back(n);
		}
		sort(arr.begin(), arr.end());
		int len = arr.size();
		int c = abs(arr[1] - arr[len - 2]);
		cout << "Test case #"<<q+1<<" \: "<<c<<endl;
		c = 0;
		

	}
}