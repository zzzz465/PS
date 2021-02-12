#include <iostream>
#include <vector>
#include <climits>

auto vect = std::vector<int>();
int memo[1000][10000];

int solve(int index, int left) {
    if (left == 0) return 0;
    if (index >= vect.size() || (index + 1) > left) return INT_MIN;

    int& max = memo[index][left];

    if (max != -1) return max;

    for (int i = 0; i * (index + 1) <= left; i++) {
        int price = vect[index] * i;
        max = std::max(max, solve(index + 1, left - (index + 1) * i) + price);
    }

    return max;
}

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < 1000; i++)
        std::fill_n(memo[i], sizeof(memo[i]) / sizeof(int), -1);

    for (int i = 0; i < T; i++) {
        int val; std::cin >> val;
        vect.push_back(val);
    }

    int result = solve(0, T);

    std::cout << result;

    return 0;
}