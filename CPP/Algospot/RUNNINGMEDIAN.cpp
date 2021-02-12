#include <iostream>
#include <vector>
#include <queue>

int A = 1983;
int a, b, N;
int MOD = 20090711;

int GetValue() {
    int temp = A;

    A = A * a;
    A %= MOD;
    A += b;
    A %= MOD;

    return temp;
}

void solve() {
    std::priority_queue<int, std::vector<int>, std::less<int>> maxHeap;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

    int ret = 0;

    for(int i = 1; i <= N; i++) {
        if (maxHeap.size() == minHeap.size())
            maxHeap.push(GetValue());
        else
            minHeap.push(GetValue());

        if (!maxHeap.empty() && !minHeap.empty() && maxHeap.top() > minHeap.top()) {
            int a = maxHeap.top(); int b = minHeap.top();
            maxHeap.pop(); minHeap.pop();
            maxHeap.push(b);
            minHeap.push(a);
        }
        ret = (ret + maxHeap.top()) % MOD;
    }

    std::cout << ret << "\n";
}

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++) {
        A = 1983;
        std::cin >> N >> a >> b;
        solve();
    }

    return 0;
}