#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int solution(int K, vector<int> A) {
    // 0번 lane은 무시
    // 라인<시간>???
    vector<set<int>> lanes = vector<set<int>>(K+1, set<int>());

    // reverse(A.begin(), A.end());
    set<int> usedLanes = set<int>();

    for (int i = 0; i < A.size(); i++) {
        int val = A[i];
        lanes[val].insert(i+1);
        usedLanes.insert(val);
    }

    int runCount = 0;
    for (auto it = usedLanes.begin(); it != usedLanes.end(); it++) {
        auto i = *it;
        while (lanes[i].size() > 0) {
            runCount += 1;
            int currLane = i;
            int currIndex = *lanes[currLane].upper_bound(0);
            lanes[i].erase(currIndex);

            do {
                currLane += 1;
                
                if (currLane <= K && lanes[currLane].size() > 0) {
                    auto currIndexIt = lanes[currLane].upper_bound(currIndex);
                    if (currIndexIt != lanes[currLane].end()) {
                        currIndex = *currIndexIt;
                        lanes[currLane].erase(currIndexIt);
                    } else {
                        break;
                    }
                } else {
                    break;
                }
            } while (true);
        }
    }

    return runCount;
}

int main() {
    auto vect = vector<int>();
    vect.push_back(1);
    vect.push_back(3);
    vect.push_back(4);
    vect.push_back(2);
    vect.push_back(5);
    int result = solution(5, vect);
    cout << result;
}