#include <iostream>
#include <vector>
#include <algorithm>

class Node;

typedef std::pair<Node*, int> weightedPair;

class Node {
public:
    int index;
    Node* parent;
    std::vector<weightedPair> connected;
    bool visit = false;
    Node(int index) {
        this->index = index;
    }

private:
    Node() { }
};

const int size = 10000 + 1;
Node* nodes[size];

void insert(int index, int otherIndex, int weight) {
    if (nodes[index] == nullptr)
        nodes[index] = new Node(index);

    if (nodes[otherIndex] == nullptr)
        nodes[otherIndex] = new Node(index);

    weightedPair p;
    p.first = nodes[otherIndex];
    p.second = weight;

    nodes[index]->connected.push_back(p);

    weightedPair p2;
    p2.first = nodes[index];
    p2.second = weight;
    nodes[otherIndex]->connected.push_back(p2);
}

int max_length = -1;

int DFS(Node* head) { 
    head->visit = true;

    std::vector<int> lengths;
    for (auto pair : head->connected)
        if (pair.first->visit != true)
            lengths.push_back(DFS(pair.first) + pair.second);

    std::sort(lengths.begin(), lengths.end());

    if (lengths.size() >= 2) {
        int temp = lengths[lengths.size() - 1] + lengths[lengths.size() - 2];
        max_length = std::max(temp, max_length);
        return lengths.back();
    } else if (lengths.size() == 1) {
        return lengths.front();
    } else {
        return 0;
    }
}

int main() {
    int V;
    std::cin >> V;

    nodes[1] = new Node(1);

    for (int i = 0; i < V - 1; i++) {
        int parent, child, weight;
        std::cin >> parent >> child >> weight;
        insert(parent, child, weight);
    }

    int result = DFS(nodes[1]);

    std::cout << std::max(result, max_length) << "\n";
    return 0;
}