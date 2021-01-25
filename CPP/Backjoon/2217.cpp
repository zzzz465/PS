#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> ropes(N, 0);

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        ropes.at(i) = val;
    }

    sort(ropes.begin(), ropes.end(), greater<int>()); // descending order

    int max_endurable_weight = 0;
    for (int i = 0; i < N; i++) {
        int endurable_weight = (i+1) * ropes.at(i);
        max_endurable_weight = max(max_endurable_weight, endurable_weight);
    }

    cout << max_endurable_weight << "\n";

    return 0;
}