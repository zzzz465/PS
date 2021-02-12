#include <iostream>
#include <cmath>
#include <climits>

using namespace std;

int memo[100001];

int solve(int n) {
    if (n == 1) return 1;
    if (n == 0) return 0;
    if (n < 0) return INT_MAX;

    int& ret = memo[n];
    if (ret != -1) return ret;

    int minVal = INT_MAX;
    for (int i = sqrt(n); i >= 1; i--)
        minVal = min(minVal, solve(n - pow(i, 2)) + 1);

    return ret = minVal;
}

int main() {
    int N;
    cin >> N;

    fill_n(memo, sizeof(memo) / sizeof(int), -1);

    int result = solve(N);
    cout << result;

    return 0;
}