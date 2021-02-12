#include <iostream>

struct Node {
    Node *left, *right;
    int value;
    Node(int value) {
        this->value = value;
        this->left = nullptr;
        this->right = nullptr;
    }
};

Node* insert(Node* head, Node* node) {
    if (head == nullptr) return node;

    if (node->value < head->value)
        head->left = insert(head->left, node);
    else
        head->right = insert(head->right, node);

    return head;
}

void DFS(Node* node) {
    if (node == nullptr) return;

    DFS(node->left);
    DFS(node->right);

    std::cout << node->value << "\n";
}

int main() {
    Node* head = nullptr;
    int value;
    while (scanf("%d", &value) != EOF) {
        Node* node = new Node(value);
        head = insert(head, node);
    }

    DFS(head);

    return 0;
}