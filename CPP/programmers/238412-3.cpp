#include <vector>
#include <algorithm>

using namespace std;

struct State {
    vector<int> common;
};

vector<State> memo;
vector<int> array;

vector<int> solve(int index) {
    if (true) { // base case

    }

    for (int other = index - 1; other >= 0; other--) {
        auto common = solve(other - 1);
        if (find(common.begin(), common.end(), other) !=)
    }
}

int solution(vector<int> a) {

}