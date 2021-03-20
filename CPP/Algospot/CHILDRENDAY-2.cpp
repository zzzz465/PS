#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

/*
    n명에게 똑같이 나누어줌, 이 때, m명에게는 1개를 더 줘야함
    즉, n-m명 에게는 k개를, m명에겐 k+1 개를 줌
    (n-m) * k + m * (k + 1) = x개
    nk - mk + mk + m = x
    nk + m = x
    즉, nk + m = x 을 달성하는 x를 구하시오, 이 때 n과 m 은 주어져있는 수, k을 최소로 해야 함
    nk = x-m
*/

using namespace std;

// typedef std::pair<int, int> myPair; // 값?
typedef long long ll;

ll solve() {
    ll d, m, n;
    cin >> d >> n >> m;

    // 초기화 및 사용가능 데이터
    vector<bool> available_numbers = vector<bool>(10, false);
    // bool available_numbers[10];
    // std::fill_n(available_numbers, 10, false);
    while (d > 0) {
        ll num = d % 10;
        available_numbers.at(num) = true;
        d /= 10;
    }

    auto q = queue<ll>();
    for (int i = 1; i < 10; i++)
        if (available_numbers.at(i))
            q.push(i);

    ll maximum = INT64_MAX / 100;

    while (q.size() > 0) {
        auto curr = q.front();
        q.pop();

        if (curr > maximum)
            return -1;

        ll minimum = n + m;

        for (int i = 0; i < 10; i++) {
            if (available_numbers.at(i)) { // 숫자 마지막에 append 하는 것으로 결정
                auto next = curr * 10 + i;
                if (next >= minimum && (next - m) % n == 0) {
                    return next;
                } else {
                    q.push(next);
                }
            }
        }
    }

    return -1;
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        ll result = solve();
        if (result != -1)
            cout << result << "\n";
        else
            cout << "IMPOSSIBLE" << "\n";
    }

    return 0;
}