#include <iostream>
#include <vector>

struct TreeNode {
    std::vector<TreeNode*> children;
    int p, q;
};

bool isChild(TreeNode* parent, int p, int q) {
    if (parent->p < p && parent->q < q)
        return true;
    else
        return false;
}

bool insert(TreeNode* root, int p, int q) {
    auto it = root->children.rbegin();
    for (; it != root->children.rend(); it++) {
        if (isChild(*it, p, q)) {
            if (insert(*it, p, q)) // 자식에서 호출
                return true;

            TreeNode* newNode = new TreeNode();
            newNode->p = p;
            newNode->q = q;

            
            return true;
        }
    }
}

void solve() {
    int N;
    std::cin >> N;
    for (int i = 0; i < N; i++) {
        int p, q; // 문제 수 p, 라면 q
        std::cin >> p >> q;


    }
}

int main() {
    int C;
    std::cin >> C;
    for (int i = 0; i < C; i++) {
        solve();
    }

    return 0;
}