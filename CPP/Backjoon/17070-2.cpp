#include <iostream>
// 깔끔한 코드로 다시 풀기
using namespace std;

const int map_size = 16;
int N, map[map_size][map_size];

// y x
int direction[3][2] = { {0, 1}, {1, 1}, {1, 0} };

int total_count = 0;

void dfs(int y, int x, int state) { // state -> 0 = 가로, 1 = 대각선, 2 = 세로
    if (y < 0 || y >= N || x < 0 || x >= N) return; // 위치가 유효하지 않음

    if (map[y][x] == 1) return; // 벽이 있는 공간에 파이프를 가져다 둠

    if (state == 1) {
        if (map[y-1][x] == 1 || map[y][x-1] == 1) // 대각선일때는 왼쪽, 윗쪽에 파이프가 있으면 안됨
            return;
    }

    if (y == N - 1 && x == N - 1) {
        total_count += 1;
        return;
    }

    switch (state) {
        case 0: {
            for (int i = 0; i <= 1; i++) {
                dfs(y + direction[i][0], x + direction[i][1], i);
            }
        } break;

        case 1: {
            for (int i = 0; i <= 2; i++) {
                dfs(y + direction[i][0], x + direction[i][1], i);
            }
        } break;

        case 2: {
            for (int i = 1; i <= 2; i++) {
                dfs(y + direction[i][0], x + direction[i][1], i);
            }
        } break;
    }
}

void solve() {
    dfs(0, 1, 0);
    cout << total_count << "\n";
}

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int val; cin >> val;
            map[i][j] = val;
        }
    }

    solve();

    return 0;
}