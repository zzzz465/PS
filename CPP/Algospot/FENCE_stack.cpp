#include <iostream>
#include <vector>
#include <stack>

std::vector<int> h;

int solveStack() {
    std::stack<int> remaining;
    h.push_back(0);
    int ret = 0;
    for (int i = 0; i < h.size(); i++) {
        while (!remaining.empty() && h[remaining.top()] >= h[i]) {
            int j = remaining.top();
            remaining.pop();
            int width = -1;

            if (remaining.empty())
                width = i;
            else
                width = (i - remaining.top() - 1);

            ret = std::max(ret, h[j] * width);
        }
        remaining.push(i);
    }

    return ret;
}

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++) {
        int N;
        std::cin >> N;
        h.clear();
        for (int j = 0; j < N; j++) {
            int val; std::cin >> val;
            h.push_back(val);
        }
        
        int result = solveStack();
        std::cout << result << "\n";
    }

    return 0;
}