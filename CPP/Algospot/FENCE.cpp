#include <iostream>
#include <vector>
#include <functional>

int main() {
    int N;
    std::cin >> N;
    
    for (int _ = 0; _ < N; _++) {
        int numberCount;
        std::cin >> numberCount;
        std::vector<int> planks;
        for (int i = 0; i < numberCount; i++) {
            int num;
            std::cin >> num;
            planks.push_back(num);
        }

        std::function<int(int, int)> solve = [&](int left, int right) -> int {
            if (left == right) return planks.at(left);

            int mid = (left + right) / 2;
            int max_size = std::max(solve(left, mid), solve(mid + 1, right));

            int low = mid, high = mid + 1;
            int height = std::min(planks[low], planks[high]);
            max_size = std::max(max_size, height * 2);

            while (left < low || high < right) {
                if (high < right && (low == left || planks[low - 1] < planks[high + 1])) {
                    high += 1;
                    height = std::min(height, planks[high]);
                } else {
                    low -= 1;
                    height = std::min(height, planks[low]);
                }
            }

            max_size = std::max(max_size, height * (high - low + 1));

            return max_size;
        };

        int max_size = solve(0, numberCount - 1);
        std::cout << max_size << std::endl;
    }

    return 0;
}