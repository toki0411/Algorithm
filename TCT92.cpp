#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> arr;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N, M, K; 
	int sum = 0;
	int a;
	cin >> N >> M >> K;
	for (int i = 0; i < N; i++) {
		cin >> a;
		arr.push_back(a);
	}
	sort(arr.begin(), arr.end());
	int max = arr[N-1];
	int r = 0;
	int c = 0;
	while(true){
		if (r == M)
			break;
		sum += arr[N - 1];
		c++;
		r++;
		if (c == K) {
			sum += arr[N - 2];
			r++;
			c = 0;
		}
	}
	cout << sum;
}