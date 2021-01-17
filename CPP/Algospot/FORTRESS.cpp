#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

int distance(int x1, int y1, int x2, int y2) {
    return pow((x2 - x1), 2) + pow((y2 - y1), 2);
}

int sqr(int x) {
    return x*x;
}

class Node {
public:
    Node* parent = nullptr;
    std::vector<Node*> childs;
    int x, y, r, depth, index;
    Node(int x, int y, int r, int index) {
        this->x = x; this->y = y; this->r = r; this->index = index;
    }

    bool insert(int x, int y, int r, int index) {
        int dist = distance(this->x, this->y, x, y);
        if (r < this->r && distance(this->x, this->y, x, y) < sqr(this->r - r)) { // 원이 내 원 내부에 있을 경우
            for (Node* node : childs) {
                if (node->insert(x, y, r, index))
                    return true;
            }

            Node* newNode = new Node(x, y, r, index);
            newNode->parent = this;
            newNode->depth = this->depth + 1;
            this->childs.push_back(newNode);
            return true;
        } else {
            return false;
        }
    }

    Node* getDeepest() {
        if (this->childs.size() > 0) {
            Node* deepest = this;
            for (auto child : this->childs) {
                auto childDeepest = child->getDeepest();
                if (childDeepest->depth > deepest->depth)
                    deepest = childDeepest;
            }

            return deepest;
        } else {
            return this; 
        }
    }

    void clear() {
        for (auto child : childs) {
            child->clear();
            delete child;
        }
    }

private:
    Node() { }
};

void solve() {
    int N; std::cin >> N;

    int rootX, rootY, rootR;
    std::cin >> rootX >> rootY >> rootR;

    Node root = Node(rootX, rootY, rootR, 0);
    root.depth = 0;

    // 첫번째는 외각의 벽
    for (int i = 1; i < N; i++) {
        int x1, y1, r1;
        std::cin >> x1 >> y1 >> r1;
        // x.push_back(x1);
        // y.push_back(y1);
        // radius.push_back(r1);

        root.insert(x1, y1, r1, i);
    }

    // 안에 있거나, 밖에 있거나 둘중 하나
    // 가장 깊은것 하나를 찾아서 BFS를 하자
    auto deepestNode = root.getDeepest();
    // BFS time
    std::queue<Node*> node_queue;
    node_queue.push(deepestNode);
    std::queue<int> depth_queue = std::queue<int>();
    depth_queue.push(0);

    std::vector<bool> visit = std::vector<bool>(N, false);
    visit[deepestNode->index] = true;

    int max_depth = -1;

    while (node_queue.size() > 0) {
        auto node = node_queue.front();
        node_queue.pop();
        auto depth = depth_queue.front();
        depth_queue.pop();

        int x, y, r, index;

        max_depth = std::max(max_depth, depth);

        if (node->parent != nullptr && visit[node->parent->index] != true) {
            x = node->parent->x;
            y = node->parent->y;
            r = node->parent->r;
            index = node->parent->index;

            node_queue.push(node->parent);
            depth_queue.push(depth + 1);
            visit[node->parent->index] = true;
        }

        for (auto child : node->childs) {
            if (visit[child->index] != true) {
                x = child->x;
                y = child->y;
                r = child->r;
                index = child->index;

                node_queue.push(child);
                depth_queue.push(depth + 1);
                visit[child->index] = true;
            }
        }
    }

    std::cout << max_depth << "\n";

    root.clear();
}

int main() {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        solve();
    }

    return 0;
}