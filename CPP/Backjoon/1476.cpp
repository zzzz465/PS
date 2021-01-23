#include <iostream>

int main() {
    int ESM[3];
    int& E = ESM[0];
    int& S = ESM[1];
    int& M = ESM[2];
    // E는 1~15, S는 1~28, M은 1~19
    std::cin >> E >> S >> M;

    // E 는 n * 15 + E
    int count = 0;

    for (int e = 0; ; e++) {
        for (int m = 0; m <= e; m++) {
            for (int s = 0; s <= m; s++) {
                int val1 = (e) * 15 + E;
                int val2 = (m) * 19 + M;
                int val3 = (s) * 28 + S;
                if (val1 == val2 && val2 == val3) {
                    std::cout << val1;
                    return 0;
                }
            }
        }
    }

    return 0;
}