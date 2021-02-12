#include <iostream>
#include <vector>
#include <algorithm>
#include <valarray>

std::vector<int> preorder, inorder;

int nodes[1000];

void solve(std::vector<int>& preorder, std::vector<int>& inorder) {
    std::vector<int> pre, in;

    int headVal = preorder[0];
    auto it = std::find(inorder.begin(), inorder.end(), headVal);

    std::slice();
}

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++) {
        int N, val;
        std::cin >> N;
        preorder.clear();
        inorder.clear();
        std::fill_n(nodes, sizeof(nodes) / sizeof(int), -1);

        for (int j = 0; j < N; j++) {
            std::cin >> val;
            preorder.push_back(val);
        }

        for (int j = 0; j < N; j++) {
            std::cin >> val;
            inorder.push_back(val);
        }

        solve();
    }

    return 0;
}