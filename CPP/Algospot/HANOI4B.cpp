#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>

using namespace std;

class State {
public:
    vector<stack<int>> sticks;
    int count = 0;
    State(vector<stack<int>> sticks) {
        this->sticks = sticks;
    }

    bool operator==(const State &rhs) const {
        return this->sticks == rhs.sticks;
    }

    bool operator<(const State &rhs) const {
        return this->sticks < rhs.sticks;
    }

    vector<State> getAdjacent() const {
        vector<State> result;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                // i에서 뽑아서 j로 옮김
                if (i == j || sticks[i].size() == 0) continue;

                if (sticks[j].size() == 0 || sticks[i].top() < sticks[j].size()) {
                    State next = State(this->sticks);
                    next.count = this->count + 1;
                    next.sticks[i].pop();
                    next.sticks[j].push(this->sticks[i].top());
                    result.push_back(next);
                }
            }
        }

        return result;
    }
};

int solve() {
    int N; cin >> N;

    State initial = State(vector<stack<int>>(4, stack<int>()));
    
    for (int i = 0; i < 4; i++) {
        vector<stack<int>> &sticks = initial.sticks;
        int count;
        cin >> count;
        for (int j = 0; j < count; j++) {
            int val; cin >> val;
            sticks[i].push(val);
        }
    }

    State end = State(vector<stack<int>>(4, stack<int>()));
    for (int i = N; i >= 1; i--) { // 마지막에 다 도달
        end.sticks[3].push(i);
    }

    auto q = queue<State>();
    q.push(initial);

    auto record = map<State, int>();

    while (q.size() > 0) {
        auto curr = q.front();
        q.pop();

        if (record.count(curr) == 0) {
            record[curr] = curr.count;

            auto adjacents = curr.getAdjacent();
            for(auto adj : adjacents) {
                if (adj == end) {
                    return adj.count;
                } else {
                    q.push(adj);
                }
            }
        }
    }

    return -1;
}

int main() {
    int C;
    cin >> C;

    for (int i = 0; i < C; i++) {
        int result = solve();
        cout << result << "\n";
    }

    return 0;
}