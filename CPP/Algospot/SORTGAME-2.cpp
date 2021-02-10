#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

map<vector<int>, int> cache;
bool calculated[8] = { false };

void preCalculate(int n) {
    if (calculated[n])
        return;

    queue<vector<int>> q;

    vector<int> initial(n, 0);
    for (int i = 0; i < n; i++)
        initial.at(i) = i;

    q.push(initial);
    cache.insert(make_pair(initial, 0));

    while (q.size() > 0) {
        auto front = q.front();
        q.pop();

        auto cost = cache[front];

        for (int i = 0; i < front.size(); i++) {
            for (int j = i + 2; j <= front.size(); j++) {
                reverse(front.begin() + i, front.begin() + j);

                if (cache.count(front) == 0) {
                    cache.insert(make_pair(front, cost + 1));
                    q.push(front);
                }

                reverse(front.begin() + i, front.begin() + j);
            }
        }
    }

    calculated[n] = true;
}

void solve() {
    int N;
    cin >> N;

    vector<int> numbers(N, 0);
    vector<int> converted(N, 0);

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        numbers.at(i) = val;
    }

    for (int i = 0; i < N; i++) {
        int less = 0;
        for (int j = 0; j < N; j++)
            if (numbers.at(j) < numbers.at(i))
                less++;
        
        converted.at(i) = less;
    }

    preCalculate(N);
    int result = cache.at(converted);

    cout << result << "\n";
}

int main() {
    int C;
    cin >> C;

    for (int i = 0; i < C; i++)
        solve();

    return 0;
}