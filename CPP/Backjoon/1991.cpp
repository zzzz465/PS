#include <iostream>

char nodes[10000]; // 0~25 A~Z 26자

int getIndex(char c) { // 대문자 A-Z
    return c - 65;
}

bool isValid(char c) {
    return 65 <= c && c <= 90;
}

void DFS_preorder(int index) {
    std::cout << nodes[index];

    if (nodes[index * 2 + 1] != -1)
        DFS_preorder(index * 2 + 1);
    
    if (nodes[index * 2 + 2] != -1)
        DFS_preorder(index * 2 + 2);
}

void DFS_inorder(int index) {
    if (nodes[index * 2 + 1] != -1)
        DFS_inorder(index * 2 + 1);
    
    std::cout << nodes[index];

    if (nodes[index * 2 + 2] != -1)
        DFS_inorder(index * 2 + 2);
}

void DFS_postorder(int index) {
    if (nodes[index * 2 + 1] != -1)
        DFS_postorder(index * 2 + 1);

    if (nodes[index * 2 + 2] != -1)
        DFS_postorder(index * 2 + 2);

    std::cout << nodes[index];
}

int find(int root, int value) {
    if (nodes[root] == value) return root;
    else if (nodes[root] == -1) return -1;

    int result = -1;
    if ((result = find(root * 2 + 1, value)) != -1)
        return result;

    return find(root * 2 + 2, value);
}

void insert(int parent, int left, int right) {
    int index = find(0, parent);
    if (isValid(left))
        nodes[index * 2 + 1] = left;
    if (isValid(right))
        nodes[index * 2 + 2] = right;
}

int main() {
    int T;
    std::cin >> T;

    std::fill_n(nodes, sizeof(nodes) / sizeof(int), -1);
    nodes[0] = (int)'A';

    for (int i = 0; i < T; i++) {
        char root, left, right;
        std::cin >> root >> left >> right;

        insert((int)root, (int)left, (int)right);
    }

    DFS_preorder(0);
    std::cout << "\n";
    DFS_inorder(0);
    std::cout << "\n";
    DFS_postorder(0);
    std::cout << "\n";

    return 0;
}