#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;

int main() {
    int N;
    cin >> N;

    vector<int> applicants(N, 0);
    for (int i = 0; i < N; i++) {
        int val; cin >> val;
        applicants.at(i) = val;
    }

    int B, C;
    cin >> B >> C;

    ll count = 0;

    for (auto applicant : applicants) {
        count += 1;
        applicant -= B;
        if (applicant > 0) {
            ll temp = ceil((double)applicant / (double)C);
            count += temp;
            applicant -= temp * C;
        }

        if (applicant > 0) {
            count += 1;
        }
    }

    cout << count;

    return 0;
}