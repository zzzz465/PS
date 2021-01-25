#include <iostream>
#include <vector>
#include <queue>
// #include <unordered_map>
#include <map>
#include <algorithm>

using namespace std;

struct State {
    int X; // 현재 위치
    int count; // 연산 횟수

    bool operator < (const State& rhs) const {
        return count < rhs.X;
    }

    bool operator == (const State& state) const {
        return state.X == X;
    }
};

int main() {
    int N; // 1 ~ N ~ 10^6
    cin >> N;

    State initial;
    initial.count = 0;
    initial.X = N;

    queue<State> q;
    q.push(initial);

    map<State, State> record;

    int minVal = 0;

    while (q.size() > 0) {
        auto state = q.front();
        q.pop();

        if (record.find(state) != record.end()) {
            auto recorded_state = record.at(state);
            if (state.count >= recorded_state.count)
                continue; // 이미 더 초과임 -> 불가능
        }

        if (state.X > 1) {
            auto newState = state;
            newState.count++;
            if (state.X % 3 == 0 && state.X >= 3) {
                auto third = newState;
                third.X /= 3;
                q.push(third);
            }

            if (state.X % 2 == 0) {
                auto half = newState;
                half.X /= 2;
                q.push(half);
            }

            newState.X--;
            q.push(newState);
        } else {
            minVal = state.count;
            break;
        }
    }

    cout << minVal << "\n";

    return 0;
}