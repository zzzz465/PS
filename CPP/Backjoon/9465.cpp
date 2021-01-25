#include <iostream>
#include <vector>

using namespace std;

vector<int> first;
vector<int> second;

int memo[100000][2];

int work(int n, int pos) { // 0은 first, 1은 second
    if (n == 0) {
        if (pos == 0) return first[0];
        else return second[0];
    }

    if (n == 1) {
        if (pos == 0) {
            return work(n-1, 1) + first[n];
        } else {
            return work(n-1, 0) + second[n];
        }
    }

    int& ret = memo[n][pos];
    if (ret != -1) return ret;

    if (n >= 2) { // n >= 2
        if (pos == 0) {
            int val1 = work(n-1, 1) + first[n];
            int val2 = max(work(n-2, 0), work(n-2, 1)) + first[n];
            ret = max(val1, val2);
        } else {
            int val1 = work(n-1, 0) + second[n];
            int val2 = max(work(n-2, 0), work(n-2, 1)) + second[n];
            ret = max(val1, val2);
        }
    }

    return ret;
}

void solve() {
    int N; cin >> N;
    first = vector<int>(N, 0);
    second = vector<int>(N, 0);

    for (int i = 0; i < 100000; i++)
        for (int j = 0; j < 2; j++)
            memo[i][j] = -1;

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        first.at(i) = val;
    }

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        second.at(i) = val;
    }

    int result = max(work(N-1, 1), work(N-1, 0));
    cout << result << "\n";
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
        solve();

    return 0;
}