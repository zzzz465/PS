#include <iostream>
#include <cstring>
#include <string>
#include <vector>

std::vector< std::vector<int> > board;
int N;

int solve(std::vector<int>& participance, int count) {
    if (count == N)
        return 1;

    int res = 0;

    for (int i = 0; i < N; i++) {
        bool flag = true;
        for (int j = 0; j < participance.size(); j++) {
            if (i == participance[j] || std::abs(participance[j] - i) == (count - j)) {
                flag = false;
                break;
            }
        }

        if (flag) {
            participance.push_back(i);
            res += solve(participance, count + 1);
            participance.pop_back();
        }
    }

    return res;
}

int main() {
    std::cin >> N;

    for (int i = 0; i < N; i++)
        board.push_back(std::vector<int>(N, 0));

    std::vector<int> v;

    int result = solve(v, 0);

    std::cout << result << "\n";

    return 0;
}



/*
a: 1 2 4
b: 3 4 7

답: 1 2 3 4 7
*/