#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

int solve(int N) {
    int zeroCount = 0;
    ll left = 1;

    for (int i = 1; i <= N; i++) {
        ll reminder = i;
        while (reminder % 10 == 0) {
            zeroCount += 1;
            reminder /= 10;
        }

        left *= reminder;
        while (left % 10 == 0) {
            zeroCount += 1;
            left /= 10;
        }
        left %= 100;
    }

    return zeroCount;
}

int main() {
    
/*
    for (int i = 0; i <= 500; i++) {
        cout << i << " result: " << solve(i) << endl;
    } */
    
    int N;
    cin >> N;

    if (N == 0) {
        cout << 0;
        return 0;
    }
    
    cout << solve(N) << "\n";

    return 0;
}