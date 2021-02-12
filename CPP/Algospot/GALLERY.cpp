#include <iostream>
#include <vector>

using namespace std;

vector< vector<int> > adj;
vector<int> checked;
vector<bool> visited;
int visitedCount = 0;

int installed = 0;

int DFS(int here) {
    if (visited[here])
        return 0;
    else
        visited[here] = true;

    int child = 0;
    for (int there = 0; there < adj[here].size(); there++) {
        if (adj[here][there] != 0) {
            if (DFS(there) > 0)
                child += 1;
        }
    }

    if (child > 0) {
        installed += 1; 
        return 0;
    }

    return 1;
}

void solve() {
    int G, H;

    checked = vector<int>(G, 0);
    adj = vector<vector<int>>(G, vector<int>(G, 0));
    visited = vector<bool>(G, 0);
}

int main() {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++)
        solve();

    return 0;
}