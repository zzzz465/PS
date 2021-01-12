#include <vector>
#include <iostream>
#include <cstring>
#include <string>

int cache[101];
const int MOD = 1000000007;

int solve(int n) {
    if (n <= 1) return 1;

    int& ret = cache[n];

    if (ret != -1) return ret;
    return ret = (solve(n-2) + solve(n-1)) % MOD;
}

int asymmetric(int n) {
    if (n % 2 != 0) {
        return (solve(n) - solve(n / 2) + MOD) % MOD;
    } else {
        int ret = solve(n);
        ret = (ret - solve(n / 2) + MOD) % MOD;
        ret = (ret - solve(n / 2-1) + MOD) % MOD;
        return ret;
    }
}

int main() {
    // std::ios::sync_with_stdio(false);

    int C;
    std::cin >> C;

    for(int i = 0; i < C; i++) {
        int N;
        std::cin >> N;

        memset(cache, -1, sizeof(cache));

        cache[1] = 1;
        cache[2] = 2;

        int result = asymmetric(N);

        std::cout << std::to_string(result) << "\n";
    }
    return 0;
}