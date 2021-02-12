#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int main() {
    int N;
    cin >> N;

    vector<int> road_length(N-1, 0);
    vector<int> fuel_prices(N, 0);

    for (int i = 0; i < N - 1; i++) {
        int val; cin >> val;
        road_length.at(i) = val;
    }

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        fuel_prices.at(i) = val;
    }

    ll pos = 0;
    ll total = 0;
    while (pos < N-1) {
        ll fuel_price = fuel_prices.at(pos);
        bool find = false;
        for (int i = pos + 1; i < N; i++) {
            if (fuel_prices.at(i) < fuel_price) {
                find = true;
                ll path_sum = 0;
                for (int j = pos; j < i; j++)
                    path_sum += road_length.at(j);

                total += (fuel_price * path_sum);
                pos = i;
                break;
            }
        }

        if (!find) { // 끝까지 간다
            ll path_sum = 0;
            for (int j = pos; j < N-1; j++)
                path_sum += road_length.at(j);

            total += (fuel_price * path_sum);
            break;
        }
    }

    cout << total << "\n";

    return 0;
}