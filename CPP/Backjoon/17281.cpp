#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int N;
vector< vector<int> > records;

// ru는 0루, 1루, 2루, 3루 가 있음
int advance(int ru[4], int dist) { // dist는 1, 2, 3, 4
    int score = 0;
    for (int i = 3; i >= 0; i--) { // 0, 1, 2 에 대하여 검색
        if (ru[i] == 1) {
            if (i + dist >= 4)
                score += 1;
            else
                ru[i + dist] = 1;
            ru[i] = 0;
        }
    }

    return score;
}

int max_score = -1;

void solve(deque<int> order) {
    order.insert(order.begin() + 3, 0);

    int outCount = 0;
    int inning = 0;

    int ru[4]; // 1루, 2루, 3루, base
    int total_score = 0;
    while (inning < N) {
        auto current = order.front();
        order.pop_front();

        auto result = records[inning][current];

        switch (result) {
            case 0: {
                outCount += 1;
                if (outCount == 3) {
                    inning += 1;
                    fill_n(ru, 4, 0);
                    outCount = 0;
                }
            } break;

            case 1:
            case 2:
            case 3:
            case 4: {
                ru[0] = 1;
                total_score += advance(ru, result);
            } break;
        }

        order.push_back(current);
    }

    max_score = max(max_score, total_score);
}

void pick(deque<int>& order) {
    for (int i = 0; i < 9; i++) {
        if (i == 0) continue; // 4번 타자는 나중에 넣음
        if (find(order.begin(), order.end(), i) == order.end()) {
            order.push_back(i);
            pick(order);
            order.pop_back();
        }
    }

    if (order.size() == 8) {
        solve(order);
    }
}

void run() {
    // 어떻게든 shuffle을 한다
    // shuffle 순서대로 큐에 집어넣고 시뮬레이션 하기
    deque<int> order;
    pick(order);
}

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        vector<int> rec;
        for (int j = 0; j < 9; j++) {
            int val; cin >> val;
            rec.push_back(val);
        }
        records.push_back(rec);
    }

    run();

    cout << max_score << "\n";

    return 0;
}