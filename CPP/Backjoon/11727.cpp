#include <iostream>
#include <vector>

int N;

int memo[1001];

int solve(int index) {
    if (index == 2) {
        return 3;
    } else if (index == 1) {
        return 1;
    }

    int& ret = memo[index];
    if (ret != -1) return ret;
    return ret = (solve(index - 1) + solve(index - 2) * 2) % 10007;
}

int main() {
    std::cin >> N;

    std::fill_n(memo, sizeof(memo) / sizeof(int), -1);
    memo[1] = 1;
    memo[2] = 3;

    int result = solve(N);

    std::cout << result;

    return 0;
}