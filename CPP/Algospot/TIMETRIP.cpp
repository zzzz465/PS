#include <iostream>
#include <vector>
#include <climits>

using namespace std;

constexpr const int INF = INT_MAX;

void solve() {
    int G, W;
    cin >> G >> W;
    vector<vector<int>> matrix = vector<vector<int>>(G, vector<int>(G, -1001));

    for(int i = 0; i < W; i++) {
        int a, b, d;
        cin >> a >> b >> d;
        matrix.at(a).at(b) = d;
        matrix.at(b).at(a) = d;
    }

    // 목표: 0 -> 1
    vector<int> upper(G, INF);
    upper.at(0) = 0;
    bool updated;
    for (int iter = 0; iter < G; iter++) {
        for (int here = 0; here < G; here++) {
            for (int there = 0; there < G; there++) {
                int cost = matrix[here][there];
                if (cost != -1001 && upper[there] > upper[here] + cost) {
                    upper[there] = upper[here] + cost;
                    updated = true;
                }
            }
        }

        if (!updated) break;
    }

    if (updated) { // 마지막 완화가 성공 -> 음의 사이클이 존재함
        cout << "INFINITY" << "\n";
    }

    if (upper[1] < INF - 100000) {
        cout << "UNREACHABLE" << "\n";
    } else {
        cout << upper[1] << "\n";
    }
}

int main() {
    int C;
    cin >> C;
    for (int i = 0; i < C; i++) {
        solve();
    }

    return 0;
}