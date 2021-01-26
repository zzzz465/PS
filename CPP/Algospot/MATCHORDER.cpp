#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

void solve() {
    int N;
    cin >> N;

    vector<int> russia(N, 0);
    list<int> korea(N, 0);

    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        russia.at(i) = val;
    }

    auto it = korea.begin();
    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        *it = val;
        it++;
    }

    korea.sort(greater<int>());
    // sort(korea.begin(), korea.end(), greater<int>());
    int win = 0;
    for (int i = 0; i < N; i++) {
        auto russia_rating = russia.at(i);

        auto it = korea.rbegin();
        while (it != korea.rend() && *it < russia_rating)
            it++;

        if (it == korea.rend())
            it = korea.rbegin();
        else
            it--;

        auto korea_rating = *it;
        korea.erase(--it.base());
        
        if (korea_rating >= russia_rating)
            win++;
    }

    cout << win << "\n";
}

int main() {
    int N; cin >> N;

    for (int i = 0; i < N; i++)
        solve();

    return 0;
}