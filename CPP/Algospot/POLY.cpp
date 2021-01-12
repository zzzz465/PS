#include <iostream>
#include <vector>
#include <string>
#include <cstring>

int map[101][101];
int N;
const int MOD = 10000000;

int poly (int n, int first) {
    if (n == first) {
        return 1;
    } else {
        int& ret = map[n][first];
        if (ret == -1) {
            ret = 0;
            for (int second = 1; second <= n - first; second++) {
                int add = second + first - 1;
                add *= poly(n-first, second);
                add %= MOD;
                ret += add;
                ret %= MOD;
            }
        }

        return ret;
    }
}

int main() {
    int C;
    std::cin >> C;
    for(int i = 0; i < C; i++) {
        std::cin >> N;

        memset(map, -1, sizeof(map));

        int polyominoCount = 0;
        for(int j = 1; j <= N; j++)
            polyominoCount += poly(N, j);

        polyominoCount %= MOD;

        std::cout << std::to_string(polyominoCount) << "\n";
    }

    return 0;
}