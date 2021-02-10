#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>

using namespace std;

struct State {
    vector<int> numbers;
};

int BFS(const vector<int>& perm) {
    int n = perm.size();
    vector<int> sorted = perm;
    sort(sorted.begin(), sorted.end());
    queue<vector<int>> q;
    map<vector<int>, int> distance;
    distance[perm] = 0;
    q.push(perm);

    while (!q.empty()) {
        vector<int> here = q.front();
        q.pop();

        if (here == sorted)
            return distance[here];

        int cost = distance[here];
        for (int i = 0; i < n; i++) {
            for (int j = i + 2; j <= n; j++) {
                reverse(here.begin() + i, here.begin() + j);
                if (distance.count(here) == 0) {
                    distance[here] = cost + 1;
                    q.push(here);
                }
            }
        }
    }
}

void solve() {
    int N;
    cin >> N;

    vector<int> numbers;
    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        numbers.push_back(val);
    }
}

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
        solve();

    return 0;
}