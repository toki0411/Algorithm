#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	int a;
	int n;
	cin >> T;
	while (T--) {
		int sum = 0;
		int YH[3] = {};
		int CS[3] = {};
		cin >> n;
		for (int i = 0; i < 3; i++) {
			cin >> a;
			YH[i] = a;
		}
		for (int i = 0; i < 3; i++) {
			cin >> a;
			CS[i] = a;
		}
		if (YH[0] >= CS[2])
			sum += CS[2];
		else
			sum += YH[0];
		if (YH[1] >= CS[0])
			sum += CS[0];
		else
			sum += YH[1];
		if (YH[2] >= CS[1])
			sum += CS[1];
		else
			sum += YH[2];
		cout <<"***"<<sum<<endl;
	}
}