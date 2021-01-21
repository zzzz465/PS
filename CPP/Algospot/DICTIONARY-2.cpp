#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int adj[26][26]; // 0 - no, 1 - adj
vector<int> seen, order;

void dfs(int i) {
    seen[i] = true;

    for (int j = 0; j < 26; j++)
        if (adj[i][j] && !seen[j])
            dfs(j);

    order.push_back(i);
}

vector<int> topologicalSort() {
    seen = vector<int>(26, 0);
    order.clear();
    for (int i = 0; i < 26; i++)
        if (!seen[i])
            dfs(i);

    reverse(order.begin(), order.end());

    for(int i = 0; i < 26; i++)
        for(int j = i+1; j < 26; j++)
            if(adj[order[j]][order[i]]) // 중요
                return vector<int>();

    return order;
}

void solve() {
    int N;
    cin >> N;

    for (int i = 0; i < 26; i++)
        fill_n(adj[i], 26, 0);

    vector<string> words;

    for(int i = 0; i < N; i++) {
        string text;
        cin >> text;
        words.push_back(text);
    }

    for (int i = 1; i < N; i++) {
        auto before = words.at(i - 1);
        auto text = words.at(i);

        int min = std::min(before.size(), text.size());

        for (int j = 0; j < min; j++) {
            if (before.at(j) != text.at(j)) {
                adj[before.at(j) - 'a'][text.at(j) - 'a'] = 1;
                break;
            }
        }
    }

    auto result = topologicalSort();

    if (result.size() > 0)
        for (auto val : result)
            cout << (char)(val + 'a');
    else
        cout << "INVALID HYPOTHESIS";
    
    cout << "\n";
}

int main() {
    int T;
    cin >> T;

    for(int i = 0; i < T; i++)
        solve();

    return 0;
}