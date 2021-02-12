#include <iostream>

int solve(int n, int wood) {
    if (wood == 1 || n == wood) return 1;

    if (wood / 2 >= n)
        return solve(n, wood / 2);

    int left = n - (wood / 2);
    return solve(left, wood / 2) + 1;
}

int main() {
    int n;
    std::cin >> n;

    int stick = 64;
    int result = solve(n, stick);

    std::cout << result;

    return 0;
}