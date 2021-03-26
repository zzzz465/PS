#include <iostream>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

typedef pair<int, pair<int, int>> pos;

char matrix[1000][20];
int cache[1000][20];

int main() {
    for (int i = 0; i < 1000; i++) {
        for (int j = 0; j < 20; j++) {
            matrix[i][j] = 'x';
            cache[i][j] = -1;
        }
    }

    int N, M;
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            char c; cin >> c;
            matrix[i][j] = c;
        }
    }

    int minimum = INT_MAX;
    auto q = queue<pos>();
    for (int j = 0; j < M; j++) {
        if (matrix[0][j] == 'c') q.push(make_pair(0, make_pair(0, j)));
    }

    while (q.size() > 0) {
        auto curr = q.front();
        int score, y, x;
        score = curr.first;
        y = curr.second.first;
        x = curr.second.second;
        q.pop();
        
        if (!(0 <= y && y < M && 0 <= x && x < N)) continue;
        else if (matrix[y][x] == 'x') continue;
        else if (cache[y][x] != -1 && score > cache[y][x]) continue;
        else if (y == M - 1 && matrix[y][x] == '.') minimum = min(minimum, score);
        else {
            cache[y][x] = score;
            if (x > 0) q.push(make_pair(score + 1, make_pair(y, x-1)));
            if (x < N - 1) q.push(make_pair(score + 1, make_pair(y, x+1)));
            if (y < M) q.push(make_pair(score, make_pair(y+1, x)));
        }
    }

    cout << (minimum != INT_MAX ? minimum : -1) << "\n";

    return 0;
}