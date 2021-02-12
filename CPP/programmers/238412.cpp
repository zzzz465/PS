#include <string>
#include <vector>
#include <list>
#include <set>1
#include <algorithm>

using namespace std;

struct State {
    list<int> numbers;
    int canBlow = 1; // 임의로 터트릴 수 있는가? 0이면 소모한 것

    bool operator < (const State& rhs) const {
        if (rhs.canBlow != canBlow)
            return canBlow < rhs.canBlow;

        if (numbers.size() > rhs.numbers.size()) return false;

        for (int i = 0; i < numbers.size(); i++) {
            if (numbers[i] < rhs.numbers[i])
                return false;
        }
    }
};

map<State, State> record;
map<int, int> available;

void DFS(const State& state) {
    if (state.numbers.size() > 1) {
        for (auto it = next(state.numbers.begin()); it != state.numbers.end(); it++) {
            auto before = prev(it);
            auto curr = it;
    
            if (*before < *curr) {
                auto newState = state;
                if (newState.canBlow == 1) {
                    auto other = newState;
                    other.numbers.erase(before);
                    other.canBlow = 0;
                    DFS(other);
                }
                newState.numbers.erase(curr);
                DFS(newState);
            } else {
                auto newState = state;
                if (newState.canBlow == 1) {
                    auto other = newState;
                    other.numbers.erase(curr);
                    other.canBlow = 0;
                    DFS(other);
                }
                newState.numbers.erase(before);
                DFS(newState);
            }
        }
    } else {

    }
}

int solution(vector<int> a) {

}