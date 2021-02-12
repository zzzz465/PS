#include <iostream>
#include <vector>

std::vector<int> infixes, postfixes;

void DFS(int infixStart, int infixEnd, int postfixHeadIndex) {
    if (infixStart > infixEnd) return;

    auto headValue = postfixes[postfixHeadIndex];
    // infix head index
    int infixHeadIndex = -1;
    for (int i = infixStart; i <= infixEnd; i++) {
        if (infixes[i] == headValue) {
            infixHeadIndex = i;
            break;
        }
    }

    int leftInfixStart = infixStart;
    int leftInfixEnd = infixHeadIndex - 1;

    int rightInfixStart = infixHeadIndex + 1;
    int rightInfixEnd = infixEnd;

    int left_postfixHeadIndex = postfixHeadIndex - (rightInfixEnd - rightInfixStart + 1) - 1;
    int right_postfixHeadIndex = postfixHeadIndex - 1;

    std::cout << headValue << " ";

    DFS(leftInfixStart, leftInfixEnd, left_postfixHeadIndex);
    DFS(rightInfixStart, rightInfixEnd, right_postfixHeadIndex);

}

void solve() {
    DFS(0, infixes.size() - 1, infixes.size() - 1);
}

int main() {
    int N;
    std::cin >> N;

    infixes = std::vector<int>(N, 0);
    postfixes = std::vector<int>(N, 0);

    for (int i = 0; i < N; i++) {
        int val; std::cin >> val;
        infixes[i] = val;
    }

    for (int i = 0; i < N; i++) {
        int val; std::cin >> val;
        postfixes[i] = val;
    }

    solve();

    return 0;
}