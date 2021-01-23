#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int M, N;
    cin >> M >> N;

    vector<bool> sieve(N + 1, 0);

    for (int i = 2; i <= N / 2; i++)
        if (sieve.at(i) != true) {
            for (int j = 2; ; j++) {
                if (i * j <= N)
                    sieve[i * j] = true;
                else
                    break;
            }
        }

    for (int i = max(2, M); i <= N; i++)
        if (sieve.at(i) != true)
            cout << i << "\n";

    return 0;
}