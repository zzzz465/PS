#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

const int max_size = 100000 + 1;

struct Node {
    int index;
    int discovered = -1;
    int dfs_end = 0;
    vector<Node*> connected;

    Node(int index) {
        this->index = index;
    }
};

Node* nodes[max_size];

int N;
int discovered_count = 0;
int dfs_end_count = 0;
void DFS(Node* node) {
    node->discovered = discovered_count++;

    for (auto other : node->connected) {
        if (other->discovered == -1)
            DFS(other);
    }
    
    node->dfs_end = dfs_end_count++;
}

int main() {
    cin >> N;

    for (int i = 1; i <= N; i++) {
        nodes[i] = new Node(i);
    }

    for (int i = 1; i < N; i++) {
        int a, b; // a와 b는 간선
        cin >> a >> b;
        nodes[a]->connected.push_back(nodes[b]);
        nodes[b]->connected.push_back(nodes[a]);
    }

    DFS(nodes[1]);

    // vector<int> dfs_order;
    stack<int> order;
    for (int i = 0; i < N; i++) {
        int value; cin >> value;
        if (order.size() > 0) {
            auto top = order.top();
        } else {
            order.push(value);
        }
        // dfs_order.push_back(value);
    }

    bool valid = true;


    if (valid)
        cout << 1;
    else
        cout << 0;

    return 0;
}