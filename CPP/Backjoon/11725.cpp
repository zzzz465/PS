#include <iostream>
#include <vector>
#include <queue>

struct Node {
    int value;
    Node* parent;
    std::vector<Node*> connected;
    bool visit;
};

const int size = 100001;

Node* nodes[size];

void insert(int a, int b) {
    if (nodes[a] == nullptr) {
        nodes[a] = new Node();
        nodes[a]->value = a;
    }

    if (nodes[b] == nullptr) {
        nodes[b] = new Node();
        nodes[b]->value = b;
    }

    nodes[a]->connected.push_back(nodes[b]);
    nodes[b]->connected.push_back(nodes[a]);
}

void DFS(Node* root) {
    root->visit = true;
    for (auto child : root->connected) {
        if (child->visit != true) {
            child->parent = root;
            DFS(child);
        }
    }
}

int main() {
    int N;
    std::cin >> N;

    std::fill_n(nodes, size, nullptr);
    Node* root = new Node();
    root->value = 1;
    nodes[1] = root;

    std::queue<std::pair<int, int>> left_queue;

    for (int i = 2; i <= N; i++) {
        int a, b;
        std::cin >> a >> b;
        insert(a, b);
    }

    DFS(nodes[1]);

    for (int i = 2; i <= N; i++) {
        std::cout << nodes[i]->parent->value << "\n";
    }

    return 0;
}