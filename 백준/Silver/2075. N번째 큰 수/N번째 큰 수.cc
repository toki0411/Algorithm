#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <functional>

using namespace std;
priority_queue <int> q;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N;
	int a;
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int k = 0; k < N; k++) {
			cin >> a;
			q.push(-a);
			if (q.size() > N)q.pop();
		}
	}
	cout <<-q.top();
}