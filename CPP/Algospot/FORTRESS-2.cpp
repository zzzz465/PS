#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

// ???????????????????????????????

struct TreeNode {
    std::vector<TreeNode*> children;
    int x, y, r, index;
};

int longest;

int height(TreeNode* root) {
    std::vector<int> heights;

    for (auto child : root->children) {
        heights.push_back(height(child));
    }

    if (heights.empty()) return 0;
    std::sort(heights.begin(), heights.end());

    if (heights.size() >= 2) {
        longest = std::max(longest, 2 + heights[heights.size() - 2] + heights[heights.size() - 1]);
    }

    return heights.back() + 1;
}

int solve(TreeNode* root) {
    longest = 0;
    int h = height(root);
    return std::max(longest, h);
}

int sqr(int x) {
	return x * x;
}

int sqrdist(int a, int b) {
	return (sqr(y[a] - y[b]) + sqr(x[a] - x[b]));
}

bool enclose(int a, int b) {
	return r[a] > r[b] && sqrdist(a, b) < sqr(r[a] - r[b]);
}

bool isChild(int parent, int child) {
	if (!enclose(parent, child))
		return false;
	for (int i = 0; i < N; i++) {
		if (i != parent && i != child && enclose(parent, i) && enclose(i, child))
			return false;
	}
	return true;
}

TreeNode* getTree(int root) {
	TreeNode* tmp = new TreeNode();
	for (int i = 0; i < N; i++) {
		if (isChild(root, i)) {
			tmp->children.push_back(getTree(i));
		}
	}
	return tmp;
}

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++) {
        int N;
        std::cin >> N;
        int x1, y1, r1;
        std::cin >> x1 >> y1 >> r1;
        TreeNode* root = new TreeNode();
        root->x = x1;
        root->y = y1;
        root->r = r1;

        for (int j = 1; j < N; j++) {
            int x, y, r;
            std::cin >> x >> y >> r;

            insert(root, x, y, r);
        }

        int result = solve(root);
        std::cout << result << "\n";
    }

    return 0;
}