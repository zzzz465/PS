#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

std::map<int, int> coords;

bool isDominated(int x, int y) {
    auto it = coords.lower_bound(x);

    if (it == coords.end()) return false;

    return y < it->second;
}

void removeDominated(int x, int y) {
    auto it = coords.lower_bound(x);

    if (it == coords.begin()) return;
    it--; // 이거 없으면 에러 뱉더라
    while (true) {
        if (it->second > y) break;

        if (it == coords.begin()) {
            coords.erase(it);
            break;
        } else {
            auto jt = it;
            jt--;
            coords.erase(it);
            it = jt;
        }
    }
}

void solve() {
    coords.clear();

    int N;
    std::cin >> N;

    int sum = 0;
    for (int i = 0; i < N; i++) {
        int x, y;
        std::cin >> x >> y;

        if (!isDominated(x, y)) {
            removeDominated(x, y);
            coords[x] = y;
            sum += coords.size();
        } else {
            sum += coords.size();
        }
    }

    std::cout << sum << "\n";
}

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++)
        solve();

    return 0;
}