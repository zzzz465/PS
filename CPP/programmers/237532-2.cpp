#include <string>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int solution(vector<int> citations) {
    sort(citations.begin(), citations.end());

    int max_h = 0;
    for (int i = 0; i < citations.size(); i++) {
        int h = citations.at(i);

        if (citations.size() - i > h) { // h번 이상 인용된 논문의 개수가 h개 이상이고
            max_h = max(max_h, h);
        }
    }

    return max_h;
}

int main() {
    vector<int> asdf { 0, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4 };
    int res = solution(asdf);
    return 0;
}