#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N,M;
	cin >> N;
	M = N;
	int c = 0;
	int cc = 0;
	bool key=false;
	while (true) {
		if (N <= 2)break;
		if ((N % 3 == 0) && (N % 5 == 0)) {
			c++;
			N -= 5;
		}
		else if ((N % 3 == 0) && (N % 5 != 0)) {
			c++;
			N -= 3;
		}
		else if ((N % 3 != 0) && (N % 5 == 0))
		{
			c++;
			N -= 5;
		}
		else if(N>=5)
		{
			c++;
			N -= 5;
		}
		else if (N >= 3) {
			c++;
			N -= 3;
		}
	}
	if(N==0)
		cout << c;
	if (N != 0)
		cout << -1;
}