#include <iostream>
#include <cstring>
#include <string>

std::string members, fans;

int solve() {
    int memberMask = 0;
    int fanMask = 0;
    for (char c : members) {
        if (c == 'M') {
            memberMask |= 1;
            memberMask = memberMask << 1;
        }
    }

    for (char c : fans) {
        if (c == 'M') {
            memberMask |= 1;
            memberMask = memberMask << 1;
        }
    }

    int count = 0;

    for (int i = 0; i + members.size() <= fans.size(); i++) {
        if (memberMask & fanMask != 0)
            count += 1;

        fanMask >> 1;
    }

    return count;
}

int main() {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        std::cin >> members >> fans;
        int result = solve();
        std::cout << result << "\n";
    }

    return 0;
}