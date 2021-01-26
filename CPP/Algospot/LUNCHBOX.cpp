#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef pair<int, int> lunchPair; // 데우는 시간, 먹는 시간

void solve() {
    int N; cin >> N;

    vector<int> lunch_boxes(N, 0);
    vector<int> time_to_eat(N, 0);

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        lunch_boxes.at(i) = val;
    }

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        time_to_eat.at(i) = val;
    }

    auto comp = [](const lunchPair& a, const lunchPair& b) { return a.first < b.first; };
    map<int, lunchPair, decltype(comp)> bst;

    for (int i = 0; i < N; i++) {
        lunchPair p;
        p.first = lunch_boxes[i];
        p.second = time_to_eat[i];
        bst[p.first] = p;
    }

    int totalTime = 0;
    int lunchTime = 0;
    int eatTime = 0;
    for (auto pair : bst) {
        if (lunchTime > 0) {
            eatTime -= lunchTime;
            totalTime += lunchTime;
        } else {
            lunchTime = 
        }
    }
}

int main() {
    int N; cin >> N;
    for (int i = 0; i < N; i++)
        solve();

    return 0;
}