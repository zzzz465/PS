#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long ll;

ll distance(int x1, int y1, int x2, int y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

int max_depth = -1;
struct Node {
    int x, y, r;

    vector<Node*> nodes;

    Node(int x, int y, int r) {
        this->x = x;
        this->y = y;
        this->r = r;
    }

    bool insert(int x, int y, int r) {
        if (include(x, y, r)) {
            for (auto child : nodes)
                if (child->insert(x, y, r)) // 만약 자식에 포함되어있을 경우
                    return true;

            auto newNode = new Node(x, y, r);
            nodes.push_back(newNode);
            return true;
        }

        return false;
    }

    bool include(int x, int y, int r) {
        double dist = distance(this->x, this->y, x, y);
        return this->r > r && (dist + (double)r) < (double)(this->r);
    }

    int depth() {
        vector<int> childNodes;
        for (auto child : this->nodes)
            childNodes.push_back(child->depth());

        sort(childNodes.begin(), childNodes.end());

        if (childNodes.size() > 2) {
            // 이 노드를 루트로 한 가장 긴 path
            auto possible_maxDepth = childNodes[childNodes.size() - 1] + childNodes[childNodes.size() - 2] + 2;
            max_depth = max(max_depth, possible_maxDepth);
            return childNodes.back() + 1;
        } else if (childNodes.size() == 1) {
            return childNodes.back() + 1;
        } else {
            return 0;
        }
    }
};

void solve() {
    int N;
    cin >> N;
    max_depth = 0;
    int x, y, r;
    cin >> x >> y >> r; // 부모
    Node root(x, y, r);

    for (int i = 1; i < N; i++) {
        cin >> x >> y >> r;
        root.insert(x, y, r);
    }

    int maxDepth = max(root.depth(), max_depth);

    cout << maxDepth << "\n";
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
        solve();

    return 0;
}