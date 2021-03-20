#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

class State {
public:
    vector<vector<int>> gameBoard;
    int blankPos[2]; // <y, x>
    int step;

    State(const vector<vector<int>> &gameBoard) {
        this->gameBoard = gameBoard;
    }

    const int movement[4][2] = {
        { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }
    };

    bool operator==(const State &rhs) const {
        return this->gameBoard == rhs.gameBoard;
    }

    bool operator<(const State &rhs) const {
        return this->gameBoard < rhs.gameBoard;
    }

    vector<State> getAdjacent() {
        vector<State> result;
        for (int i = 0; i < 4; i++) {
            int offsetX = movement[i][0];
            int offsetY = movement[i][1];
            int newY = this->blankPos[0] + offsetY;
            int newX = this->blankPos[1] + offsetX;

            if (valid(newY, newX)) {
                State next = State(this->gameBoard);
                next.step = this->step + 1;
                // swap
                int& a = next.gameBoard[this->blankPos[0]][this->blankPos[1]];
                int& b = next.gameBoard[newY][newX];
                int temp = a;
                a = b;
                b = temp;
    
                result.push_back(next);
            }
        }

        return result;
    }

    bool valid(int y, int x) {
        return 0 <= y && y < 16 && 0 <= x && x < 16;
    }
};

int sgn(int x) {
    if (x == 0)
        return 0;

    return x > 0 ? 1 : -1;
}

int incr(int x) {
    return x < 0 ? x-1 : x+1;
}

int bidirectional(State start, State finish) {
    map<State, int> c;
    queue<State> q;
    if (start == finish) return 0;
    q.push(start); c[start] = 1;
    q.push(finish); c[finish] = -1;

    while (q.size() > 0) {
        State here = q.front();
        q.pop();

        vector<State> adjacent = here.getAdjacent();
        for (int i = 0; i < adjacent.size(); i++) {
            map<State, int>::iterator it = c.find(adjacent[i]);
            if (it == c.end()) { // cannot find
                c[adjacent[i]] = incr(c[here]);
                q.push(adjacent[i]);
            } else if (sgn(it->second) != sgn(c[here])) {
                return abs(it->second) + abs(c[here]) - 1;
            }
        }
    }

    return -1;
}

int main() {

}