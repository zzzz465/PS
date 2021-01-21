#include <iostream>
#include <vector>
#include <queue>

const int max_size = 15;
int N, M, D;

std::vector<std::vector<int>> initial; // N * M 배열

typedef std::pair<int, std::pair<int, int>> Point; // distance, <x, y>

Point createPoint(int distance, int x, int y) {
    return Point(distance, std::pair<int, int>(x, y));
}

int distance(int x1, int y1, int x2, int y2) {
    return abs(x2 - x1) + abs(y2 - y1);
}

int movement[3][2] = { {-1, 0}, {0, -1}, {1, 0} }; // 순서대로 왼쪽, 윗쪽, 오른쪽

int max_count = -1;

void simulate(std::vector<std::vector<int>> board, const std::vector<int>& archors) {
    int count = 0;
    int loop = 0;
    while (loop++ < N) {
        for (auto archorIndex : archors) {
            // BFS
            std::queue<Point> q = std::queue<Point>();
            q.push(createPoint(1, archorIndex, N - 1)); // 궁수 바로 위 선택
            bool visit[max_size][max_size];

            for (int i = 0; i < max_size; i++)
                for (int j = 0; j < max_size; j++)
                    visit[i][j] = false;
            
            visit[N-1][archorIndex] = true;

            while (!q.empty()) {
                int size = q.size(); // 갑자기 size가 UB로 변함
                Point point = q.front();
                q.pop();

                int distance, x, y;
                distance = point.first;
                x = point.second.first;
                y = point.second.second;

                if (0 <= x && x < M && 0 <= y && y < N) {
                    if (board[y][x] != 0 && distance <= D) { // 이 적을 공격함
                        board[y][x] = 2;
                        break;
                    }
    
                    for (int i = 0; i < 3; i++) {
                        if (visit[y + movement[i][1]][x + movement[i][0]] != true) {
                            visit[y + movement[i][1]][x + movement[i][0]] = true;
                            q.push(createPoint(distance + 1, x + movement[i][0], y + movement[i][1]));
                        }
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 2) {
                    board[i][j] = 0;
                    count += 1;
                }
            }
        }

        for (auto& last : board[N - 1]) // 마지막 줄은 이제 필요가 없음
            last = 0;

        for (int i = N - 2; i >= 0; i--) { // 아래로 한 칸 이동
            for (int j = 0; j < M; j++) {
                board[i+1][j] = board[i][j];
                board[i][j] = 0;
            }
        }
    }

    max_count = std::max(max_count, count);
}

void place(std::vector<int>& archors, int index, int left) {
    if (left == 0) // 조건 만족
        simulate(initial, archors);

    if (index >= M) // 범위 밖
        return;

    place(archors, index + 1, left); // 이 index 를 건너뜀
    archors.push_back(index); // 선택
    place(archors, index + 1, left-1);
    archors.pop_back(); // 복구
}

void solve() {
    // 바로 밑에 배치하는 경우의 수
    std::vector<int> archors;
    place(archors, 0, 3);

    std::cout << max_count << "\n";
}

int main() {
    std::cin >> N >> M >> D;

    for (int i = 0; i < N; i++) {
        std::vector<int> row;
        for (int j = 0; j < M; j++) {
            int val; std::cin >> val;
            row.push_back(val);
        }

        initial.push_back(row);
    }

    solve();

    return 0;
}