#include <iostream>
#include <vector>
#include <climits>
#include <queue>
#include <algorithm>

const int size = 20; // 최대 20까지

int map[size * size];

int N;

// 9 아기상어 위치
// 0 빈칸
// 1, 2, 3, 4, 5, 6 -> 물고기 크기

// 1) 자기보다 크기가 작은 물고기만 먹을수 있음
// 1-1) 여러마리일경우 윗쪽, 왼쪽에 있는 것을 먹음 (=index가 최소인 것)
// 자기보다 클경우 통과 X, 자기랑 사이즈 같을경우 통과 가능
// 2) 그 물고기가 있는 곳은 지나갈 수 있음
// 3) 물고기를 먹으면 크기가 1 증가함
// 3-1) 크기 N의 상어는 N개의 물고기를 먹으면 N+1 사이즈로 증가
// 먹는 물고기의 사이즈는 고려하지 않나봄?

// 상어 상태
int sharkSize = 2;
int curIndex = 0;
int lifetime = 0;
int eatCount = 0;

int minIndex = -1;
int minPath = INT_MAX;

void BFS(int);

// 가장 가까운 물고기를 먹고, 만약 거리가 동일하다면 왼쪽 위부터 먹음
void find() {
    BFS(curIndex);
}

bool isValid(int index) {
    return 0 <= index && index < N * N;
}

bool visit[size * size];
int BFSMap[size * size];

bool compare(std::pair<int, int> a, std::pair<int, int> b) {
    return a.first == b.first ? a.first > b.first : a.second > b.second;
}

void BFS(int start) {
    std::queue<int> q;

    std::fill_n(visit, N * N, false);
    std::fill_n(BFSMap, N * N, 0);
    minIndex = -1;

    q.push(start);
    visit[start] = true;

    std::vector< std::pair<int, int> > fishes; // pair<걸리는 시간, index>


    while (q.size() > 0) {
        int index = q.front();

        if (map[index] < sharkSize && map[index] != 0 && index != curIndex) {
            std::pair<int, int> p;
            p.first = BFSMap[index]; // 걸리는 길이
            p.second = index; // 상단 왼쪽 위치
            fishes.push_back(p);
        }

        // top
        int topIndex = index - N;
        if (isValid(topIndex) && visit[topIndex] != true && map[topIndex] <= sharkSize) {
            visit[topIndex] = true;
            BFSMap[topIndex] = BFSMap[index] + 1;
            q.push(topIndex);
        }

        // left
        int leftIndex = index - 1;
        if (isValid(leftIndex) && visit[leftIndex] != true && index % N != 0 && map[leftIndex] <= sharkSize) {
            visit[leftIndex] = true;
            BFSMap[leftIndex] = BFSMap[index] + 1;
            q.push(leftIndex);
        }

        // right
        int rightIndex = index + 1;
        if (isValid(rightIndex) && visit[rightIndex] != true && rightIndex % N != 0 && map[rightIndex] <= sharkSize) {
            visit[rightIndex] = true;
            BFSMap[rightIndex] = BFSMap[index] + 1;
            q.push(rightIndex);
        }

        // down
        int downIndex = index + N;
        if (isValid(downIndex) && visit[downIndex] != true && map[downIndex] <= sharkSize) {
            visit[downIndex] = true;
            BFSMap[downIndex] = BFSMap[index] + 1;
            q.push(downIndex);
        }

        q.pop();
    }

    if (fishes.size() > 0) {
        std::sort(fishes.begin(), fishes.end(), compare);
        auto first_elem = fishes.front();
        minPath = first_elem.first;
        minIndex = first_elem.second;
    }
}

void loop() {
    while (true) {
        // 가장 index가 작은 것 들 중에서 먹을 수 있는 물고기 검색
        find(); // O(n^2 * n)?
        if (minIndex == -1) break; // 목표 X

        // if (target == -1) break;

        // path 찾기, 동시에 이동
        // visit 초기화 해줘야하나?

        // if (res == INVALID_VALUE) break;

        lifetime += minPath; // 이동하는데 걸린 시간

        // 이동
        int temp = curIndex;
        curIndex = minIndex;
        map[temp] = 0;

        // 먹기
        map[curIndex] = 0;
        eatCount += 1;

        // 사이즈 업?
        if (eatCount == sharkSize) {
            sharkSize += 1;
            eatCount = 0;
        }
    }

    std::cout << lifetime << "\n";
}

int main() {
    std::cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int val; std::cin >> val;
            int index = N * i + j;
            map[index] = val;
            if (val == 9) {
                curIndex = index;
                map[index] = 0;
            }
        }
    }

    loop();

    return 0;
}