#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void DFS(vector<int> prefixes, vector<int> infixes) {
    if (prefixes.size() == 0) return;

    int head = prefixes.front();
    auto infixHeadIt = find(infixes.begin(), infixes.end(), head);

    auto leftInfixes = vector<int>(infixes.begin(), infixHeadIt); // end Index will **not** be included
    auto rightInfixes = vector<int>(infixHeadIt + 1, infixes.end());

    auto leftPrefixes = vector<int>(prefixes.begin() + 1, prefixes.begin() + 1 + leftInfixes.size());
    auto rightPrefixes = vector<int>(prefixes.begin() + 1 + leftInfixes.size(), prefixes.end());

    DFS(leftPrefixes, leftInfixes);
    DFS(rightPrefixes, rightInfixes);

    cout << head << " ";
}

void run() {
    int N;
    cin >> N;

    vector<int> prefixes;
    vector<int> infixes;

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        prefixes.push_back(val);
    }

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        infixes.push_back(val);
    }

    DFS(prefixes, infixes);
    cout << "\n";
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
        run();

    return 0;
}