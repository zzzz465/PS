#include <iostream>
#include <vector>
#include <string>
#include <climits>

using namespace std;

string input;

int max_val = INT_MIN;

int calculate(char op, int val1, int val2) {
    if (op == '+')
        return val1 + val2;

    if (op == '-')
        return val1 - val2;

    if (op == '*')
        return val1 * val2;

    return 0;
}

void DFS(int index, int acc) {
    if (index >= input.size()) {
        max_val = max(max_val, acc);
        return;
    }

    char op = index == 0 ? '+' : input[index - 1];
    char a, b;
    DFS(index + 2, calculate(op, acc, input[index] - '0')); // 안묶었을 경우

    if (index < input.size() - 2) {
        int val1 = acc;
        int val2 = calculate(input[index + 1], input[index] - '0', input[index + 2] - '0');
        DFS(index + 4, calculate(op, val1, val2));
    }
}

void solve() {
    DFS(0, 0);
}

int main() {
    int N; cin >> N;
    cin >> input;

    solve();

    cout << max_val << "\n";

    return 0;
}