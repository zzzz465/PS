#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 26 * 26
vector< vector< vector<string> > > adj;

void DFS(int pos, vector<string>& circuit) {
    vector<string> texts;
    for (int other = 0; other < 26; other++) {
        while (adj[pos][other].size() > 0) {
            texts.push_back(adj[pos][other].back());
            adj[pos][other].pop_back();
            DFS(other, circuit);
        }
    }
    
    circuit.insert(circuit.end(), texts.rbegin(), texts.rend());
}

void solve() {
    adj = vector<vector<vector<string>>>(26, vector<vector<string>>(26, vector<string>()));

    vector<string> words;
    int N; cin >> N;

    for(int i = 0; i < N; i++) {
        string text; cin >> text;
        words.push_back(text);

        char start, end;
        start = text.front();
        end = text.back();

        adj[start - 'a'][end - 'a'].push_back(text);
    }

    auto copy_adj = adj;

    int start = words.front()[0] - 'a';
    vector<string> circuit;
    DFS(start, circuit);

    reverse(circuit.begin(), circuit.end());

    for(int i = 0; i < 26; i++)
        for(int j = 0; j < 26; j++)
            if (adj[i][j].size() > 0) {
                cout << "IMPOSSIBLE" << "\n";
                return;
            }

    if (circuit.size() > 1 && *circuit.begin() == *circuit.rbegin()) {
        cout << "IMPOSSIBLE" << "\n";
        return;
    }

    char end = circuit[0].back();

    bool valid = true;

    for (int i = 1; i < circuit.size(); i++) {
        string word = circuit[i];
        char start;
        start = word.front();

        if (end != start) {
            valid = false;
            break;
        }
        else
            end = word.back();
    }
    
    if (valid) {
        for (auto str : circuit)
            cout << str << " ";
        cout << "\n";
    } else {
        cout << "IMPOSSIBLE" << "\n";
    }
}

int main() {
    int C;
    cin >> C;

    for (int i = 0; i < C; i++)
        solve();

    return 0;
}