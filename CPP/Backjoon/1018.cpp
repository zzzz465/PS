#include <iostream>
#include <vector>

using namespace std;

int N, M; // M개의 줄이 N개, 세로 N 가로 M

vector< vector<char> > board;
int min_count = 987654321;

void solve(int y, int x, vector< vector<char> > board, bool white) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if ((i + j) % 2 == 0) { // 첫번째
                if (white) {
                    if (board[y + i][x + j] != 'W') {
                        count += 1;
                    }
                } else {
                    if (board[y + i][x + j] != 'B') {
                        count += 1;
                    }
                }
            } else {
                if (white) {
                    if (board[y + i][x + j] != 'B') {
                        count += 1;
                    }
                } else {
                    if (board[y + i][x + j] != 'W') {
                        count += 1;
                    }
                }
            }
        }
    }

    min_count = min(min_count, count);
}

void run() {
    for (int i = 0; i <= N - 8; i++) {
        for (int j = 0; j <= M - 8; j++) {
            solve(i, j, board, true);
            solve(i, j, board, false);
        }
    }

    cout << min_count << "\n";
}

int main() {
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        vector<char> line;
        for (int j = 0; j < M; j++) {
            char val; cin >> val;
            line.push_back(val);
        }

        board.push_back(line);
    }

    run();

    return 0;
}