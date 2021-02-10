#include <iostream>
#include <vector>

using namespace std;

enum Status {
    LEAF = 0,
    CCTV = 1,
    WATCHED = 2
};

vector<int> galleries;
vector<int> visited;
vector<vector<int>> adj;
int g, h;

int total_cctv_count = 0;

Status DFS(int index) {
    if (visited[index] == 1)
        return WATCHED;
    else
        visited[index] = 1;

    auto this_status = LEAF;

    for (int i = 0; i < g; i++) {
        if (adj[index][i] != 0) {
            auto other_status = DFS(i);
            if (other_status == LEAF)
                this_status = CCTV;
            else if (other_status == CCTV && this_status != CCTV)
                this_status = WATCHED;
        }
    }

    if (this_status == CCTV)
        total_cctv_count += 1;

    return this_status;
}

void solve() {
    cin >> g >> h;

    visited = galleries = vector<int>(g, 0);
    adj = vector<vector<int>>(g, vector<int>(g, 0));
    total_cctv_count = 0;

    for (int i = 0; i < h; i++) {
        int a, b;
        cin >> a >> b;
        adj[a][b] = 1;
        adj[b][a] = 1;
    }

    for (int i = 0; i < g; i++) {
        auto status = DFS(i);
        if (status == LEAF)
            total_cctv_count += 1;
    }

    cout << total_cctv_count << "\n";
}

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
        solve();

    return 0;
}