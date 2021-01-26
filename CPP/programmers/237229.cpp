#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;

ll solution(int w, int h) {
    ll answer = 1;

    ll total = w * h;
    ll take = ceil((double)h / (double)w);

    answer = total - (take * w);

    return answer;
}

int main() {
    int w, h;
    w = 100000000;
    h = 100000000;
    // 1억 * 1억이면 1억*1억 - 1억 반환해야함

    ll result = solution(w, h);

    bool check = result == w * w - 100000000;

    return 0;
}