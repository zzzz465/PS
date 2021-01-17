#include <iostream>
#include <vector>

typedef int KeyType;
struct Node {
    KeyType key;
    int priority, size; // 노드의 우선순위, 그리고 서브트리의 크기
    Node *left, *right; // 좌/우 노드
    // 생성자 무엇???
    Node(const KeyType& _key) : key(_key), priority(rand()), size(1), left(NULL), right(NULL) {

    }

    void setLeft(Node* newLeft) { left = newLeft; calcSize(); }
    void setRight(Node* newRight) { right = newRight; calcSize(); }

    void calcSize() {
        size = 1;
        if (left) size += left->size;
        if (right) size += right->size;
    }
};

typedef std::pair<Node*, Node*> NodePair;

NodePair split(Node* root, KeyType key) {
    if (root == NULL) return NodePair(NULL, NULL);

    if (root->key < key) {
        auto pair = split(root->right, key);
        root->setRight(pair.first);

        return NodePair(root, pair.second);
    }

    auto pair = split(root->left, key);
    root->setLeft(pair.second);
    return NodePair(pair.first, root);
}

Node* insert(Node* root, Node* node) {
    if (root == NULL) return node;

    if (root->priority < node->priority) {
        NodePair splitted = split(root, node->key);
        node->setLeft(splitted.first);
        node->setRight(splitted.second);
        return node;
    } else if (node->key < root->key) {
        root->setLeft(insert(root->left, node));
    } else {
        root->setRight(insert(root->right, node));
    }

    return root;
}

// 노드 추가는 root = insert(root, new Node(value));
// max(a) < min(b) 일때
Node* merge(Node* a, Node* b) {
    if (a == NULL) return b;
    if (b == NULL) return a;

    if (a->priority < b->priority) {
        b->setLeft(merge(a, b->left));
        return b;
    }
    a->setRight(merge(a->right, b));
    return a;
}

Node* erase(Node* root, KeyType key) {
    if (root == NULL) return root;
    if (root->key == key) {
        Node* ret = merge(root->left, root->right);
        delete root;
        return ret;
    }

    if (key < root->key)
        root->setLeft(erase(root->left, key));
    else
        root->setRight(erase(root->right, key));
    
    return root;
}

Node* kth(Node* root, int k) {
    int leftSize = 0;
    if (root->left != NULL) leftSize = root->left->size;
    if (k <= leftSize) return kth(root->left, k);
    if (k == leftSize + 1) return root;
    return kth(root->right, k - leftSize - 1);
}

int countLessThan(Node* root, KeyType key) {
    if (root == NULL) return 0;
    if (root->key >= key)
        return countLessThan(root->left, key);
    int ls = (root->left ? root->left->size : 0);
    return ls + 1 + countLessThan(root->right, key);
}