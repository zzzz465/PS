#include <iostream>
#include <vector>
#include <limits>

std::vector<int> vect;
int T;
int min_int = -1001;

int memo[100000];

int solve(int index) {
    if (index >= vect.size())
        return min_int;

    int& ret = memo[index];

    if (ret != min_int) return ret;

    ret = solve(index + 1);
    if (ret == min_int)
        return ret = vect[index];

    else
        return ret = std::max(vect[index], vect[index] + ret);
}

int main() {
    /*
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    */
    std::cin >> T;

    // 초기화
    std::fill_n(memo, sizeof(memo) / sizeof(int), min_int);

    for (int i = 0; i < T; i++) {
        int val;
        std::cin >> val;
        vect.push_back(val);
    }

    solve(0);

    int max_val = min_int;
    for (int i = 0; i < 100000; i++)
        max_val = memo[i] > max_val ? memo[i] : max_val;

    std::cout << max_val;

    return 0;
}