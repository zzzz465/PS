#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <climits>
#include <set>

using namespace std;

constexpr const int NUMERIC_LIMIT = INT_MAX / 10;

int solve() {
    string d;
    int n, m;
    cin >> d >> n >> m;

    vector<int> available_numbers;
    queue<int> q;
    for (char c : d) {
        available_numbers.push_back(c - '0');
        q.push(c - '0');
    }

    set<int> record;
    int MINIMUM_COUNT = n + m;

    while (q.size() > 0) {
        auto front = q.front();
        q.pop();

        if (front >= NUMERIC_LIMIT) {
            continue;
        } else {
            if (front >= MINIMUM_COUNT && (front - m) % (n) == 0) { // found
                return front;
            }
        }

        for (auto val : available_numbers) {
            int newVal = front * 10; // 자릿수 밀기
            newVal += val;
            if (record.count(newVal) == 0) {
                q.push(newVal);
                record.insert(newVal);
            }
        }

        if (record.size() >= 100000)
            record.clear();
    }

    return -1;
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int result = solve();
        if (result != -1) {
            cout << result << "\n";
        } else {
            cout << "IMPOSSIBLE" << "\n";
        }
    }

    return 0;
}