#include <iostream>
#include <vector>
#include <climits>
#include <queue>
#include <algorithm>

int N, M; // 세로, 가로

/*
struct compare {
    bool operator()(std::pair<int, int> a, std::pair<int, int> b) {
        return a.first > b.first;
    }
};
*/

std::vector<int> map;
std::vector<int> dijkstra;
std::vector<bool> visit;
// std::priority_queue< std::pair<int, int>, std::vector<std::pair<int, int>>, compare> pq; // pair<key, index>

int getIndex(int y, int x) {
    return M * y + x;
}

bool isValidIndex(int index) {
    return 0 <= index && index < map.size();
}

int solve() {
    int y = 0, x = 0;

    while (true) {
        int index = -1;
        int maxVal = INT_MAX;
        // int len = M * N; // 불필요한 최적화 아닌가?
        for (int i = 0; i < M * N; i++) {
            if (visit[i] != true && dijkstra[i] < maxVal) {
                index = i;
                maxVal = dijkstra[i];
            }
        }

        if (index == -1)
            break;
        
        // top
        int topIndex = index - M;
        if (isValidIndex(topIndex) && visit[topIndex] != true) {
            int cost = map[topIndex] == 1 ? 2 : 1;
            if (dijkstra[index] + cost < dijkstra[topIndex])
                dijkstra[topIndex] = dijkstra[index] + cost;
        }

        // right
        int rightIndex = index + 1;
        if (isValidIndex(rightIndex) && index % M != M && visit[rightIndex] != true) {
            int cost = map[rightIndex] == 1 ? 2 : 1;
            if (dijkstra[index] + cost < dijkstra[rightIndex])
                dijkstra[rightIndex] = dijkstra[index] + cost;
        }

        // bottom
        int bottomIndex = index + M;
        if (isValidIndex(bottomIndex) && visit[bottomIndex] != true) {
            int cost = map[bottomIndex] == 1 ? 2 : 1;
            if (dijkstra[index] + cost < dijkstra[bottomIndex])
                dijkstra[bottomIndex] = dijkstra[index] + cost;
        }

        // left
        int leftIndex = index - 1;
        if (isValidIndex(leftIndex) && index % M != 0 && visit[leftIndex] != true) {
            int cost = map[leftIndex] == 1 ? 2 : 1;
            if (dijkstra[index] + cost < dijkstra[leftIndex])
                dijkstra[leftIndex] = dijkstra[index] + cost;
        }

        visit[index] = true;
    }

    return dijkstra[M * N - 1];
}

int main() {
    std::cin >> M >> N;

    map = std::vector<int>(M * N, 0);
    dijkstra = std::vector<int>(M * N, INT_MAX);
    dijkstra[0] = 0; // 0, 0
    visit = std::vector<bool>(M * N, false);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            char input; std::cin >> input;
            int val = input == '1' ? 1 : 0;
            map[getIndex(i, j)] = val;
        }
    }

    // 0만 있을 때 최단경로 -> (M + N - 2)
    int result = solve();
    
    std::cout << result - M - N + 2;

    return 0;
}