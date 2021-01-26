#include <string>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

struct State {
    string text;
    int cost = 0;
    int cursorIndex = 0; // cursorIndex
};

int moveIndex(int index, int size, bool increment) {
    if (increment) {
        if (index == size - 1)
            return 0;
        else
            return index + 1;
    } else {
        if (index == 0)
            return size - 1;
        else
            return index - 1;
    }
}

int solution(string name) {
    int answer = 0;

    // queue<State> q;
    State initial;
    initial.text = string(name.size(), 'A');
    initial.cost = 0;
    initial.cursorIndex = 0;
    int textLen = name.size();

    // 그리디 방법도 알아야하고, 그리디 할때 코드를 어떻게 작성해야하는지도 알아야함
    // 그리디 vs BFS 구분을 할 줄 알아야 함!!!

    auto state = initial;
    while (true) {

        if (state.text[state.cursorIndex] != name[state.cursorIndex]) {
            char c = name[state.cursorIndex];
            // 91은 Z 다음
            int cost = min(abs(c - 'A'), abs(91 - c));
            state.cost += cost;
            state.text[state.cursorIndex] = name[state.cursorIndex];
        }

        if (state.text == name) break;
        for (int i = 1; i < state.text.size(); i++) {
            int rightIndex = (state.cursorIndex + i) % textLen;
            if (state.text[rightIndex] != name[rightIndex]) {
                state.cursorIndex = rightIndex;
                state.cost += i;
                break;
            }

            int leftIndex = (state.cursorIndex - i + textLen) % textLen;
            if (state.text[leftIndex] != name[leftIndex]) {
                state.cursorIndex = leftIndex;
                state.cost += i;
                break;
            }
        }
    }

    return state.cost;
}

int main() {
    int val = (-1 % 3);

    int result = solution("JEROEN");

    bool res[9];

    res[0] = solution("JAN") == 23;
    res[1] = solution("JEROEN") == 56;
    res[2] = solution("AABAAAAAAAB") == 6;
    res[3] = solution("AAAAAAAA") == 0;
    res[4] = solution("ABBBBAAAABAA") == 14;
    res[5] = solution("ABAAAAAAABA") == 6;
    res[6] = solution("AAB") == 2;
    res[7] = solution("AABAAAAAAABBB") == 12;
    res[8] = solution("ZZZ") == 5;

    return 0;
}