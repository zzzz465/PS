#include <iostream>
#include <vector>
#include <climits>

using namespace std;

const int max_size = 10;
const int max_index = max_size * max_size;

int board[max_size][max_size];

bool canPlace(int y, int x, int size) {
    if (y <= max_size - size && x <= max_size - size) {
        for (int i = y; i < y + size; i++)
            for (int j = x; j < x + size; j++)
                if (board[i][j] != 1)
                    return false;

        return true;
    }

    return false;
}

void add(int y, int x, int size, int value) {
    for (int i = y; i < y + size; i++)
        for (int j = x; j < x + size; j++)
            board[i][j] += value;
}

// 크기 0짜리 종이는 0으로 설정, 나머지는 n번째 = n*n 종이
int papers[] = { 0, 5, 5, 5, 5, 5 };

int min_use = INT_MAX;

void solve(int index) {
    while (index < max_index) {
        int y, x;
        y = index / max_size;
        x = index % max_size;

        if (board[y][x] == 1) {
            for (int i = 1; i <= 5; i++) {
                if (canPlace(y, x, i) && papers[i] > 0) {
                    papers[i] -= 1;
                    add(y, x, i, 1);
                    solve(index + i);
                    add(y, x, i, -1);
                    papers[i] += 1;
                }
            }

            return; // 지우지 못함, 즉 종료
        } else {
            index += 1;
        }
    }

    // index 최대치까지 도달하였음
    int count = 25;
    for (int i = 1; i <= 5; i++)
        count -= papers[i];

    min_use = min(min_use, count);
}

void run() {
    solve(0);
    if (min_use != INT_MAX)
        cout << min_use << "\n";
    else
        cout << -1 << "\n";
}

int main() {

    for (int i = 0; i < max_size; i++) {
        for (int j = 0; j < max_size; j++) {
            int val; cin >> val;
            board[i][j] = val;
        }
    }

    run();

    return 0;
}