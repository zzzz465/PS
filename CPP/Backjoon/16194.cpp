#include <iostream>
#include <vector>
#include <climits>

auto vect = std::vector<int>();
int memo[1000][10000];

int solve(int index, int left) {
    if (left == 0) return 0;
    if (index >= vect.size() || (index + 1) > left) return INT_MAX;

    int& min = memo[index][left];

    if (min != -1) return min;
    min = INT_MAX;

    for (int i = 0; i * (index + 1) <= left; i++) {
        int price = vect[index] * i;
        int res = solve(index + 1, left - (index + 1) * i);
        if (res != INT_MAX)
            min = std::min(min, res + price);
    }

    return min;
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