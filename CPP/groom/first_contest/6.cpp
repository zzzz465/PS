#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;
ll cache[10000][100] = { -1, };
int clothes[10000][100] = { -1, };

using namespace std;
int N, M;

int solve(int y, int x) {
    if (!(0 <= y && y < M && 0 <= x && x < N)) return 0;

    if (cache[y][x] == -1) {
        int result = max(solve(y-1, x), solve(y, x-1));
        cache[y][x] = result + clothes[y][x];
    }

    return cache[y][x];
}

int main() {
    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            int val; cin >> val;
            cache[i][j] = -1;
            clothes[i][j] = val;
        }
    }

    cout << solve(M-1, N-1) << "\n";

    return 0;
}