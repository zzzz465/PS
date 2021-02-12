#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector< vector<char> > board;
vector< vector<bool> > visited;
vector< vector<int> > discovered;
int N, M;

int direction[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; // 왼 오른 아래 위
int discovered_count = 0;

bool isValid(int y, int x) {
    return 0 <= y && y < N && 0 <= x && x < M;
}

typedef pair<int, int> Pos;

stack<Pos> record;
void DFS(int y, int x, char kind) {
    discovered[y][x] = discovered_count++;

    for (int i = 0; i < 4; i++) {
        int newY = y + direction[i][0];
        int newX = x + direction[i][1];

        if (record.size() > 0) {
            auto top = record.top();
            if (top == Pos(newY, newX))
                continue; // 바로 이전 위치는 고려대상이 아님
        }

        if (isValid(newY, newX) && board[newY][newX] == kind) {
            if (discovered[newY][newX] == -1) {
                record.push(Pos(y, x));
                DFS(newY, newX, kind);
                record.pop();
            }
            else if (discovered[newY][newX] != -1 && discovered[newY][newX] < discovered[y][x]) { // 이전에 미리 방문함
                if (visited[newY][newX]) { // 교차 간선

                } else { // 역방향 간선 = 사이클!!!!!
                    cout << "Yes";
                    exit(0);
                }
            }
        }
    }

    visited[y][x] = true;
}

void solve() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (discovered[i][j] == -1) {
                discovered_count = 0;
                DFS(i, j, board[i][j]);
            }
        }
    }
}

int main() {
    cin >> N >> M;

    board = vector<vector<char>>(N, vector<char>(M, 0));
    discovered = vector<vector<int>>(N, vector<int>(M, -1));
    visited = vector<vector<bool>>(N, vector<bool>(M, false));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            char c; cin >> c;
            board[i][j] = c;
        }
    }

    solve();

    cout << "No";

    return 0;
}