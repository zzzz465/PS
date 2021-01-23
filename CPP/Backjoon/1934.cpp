#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int gcd(int a, int b) {
    if (b > a) return gcd(b, a);

    while (b != 0) {
        int n = a % b;
        a = b;
        b = n;
    }

    return a;
}

void solve() {
    int A, B;
    cin >> A >> B;

    int gcdValue = gcd(A, B);

    cout << A * B / gcdValue << "\n";
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
        solve();

    return 0;
}