#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int solution(vector<int> priorities, int location) {
    deque<int> q = deque<int>();
    for (int i = 0; i < priorities.size(); i++)
        q.push_back(i);

    int printedCount = 0;

    while (true) {
        int toBePrinted = q.front();
        q.pop_front();
        
        bool higherPriorityExist = false;
        for(auto it = q.begin(); it != q.end(); it++) {
            if (priorities[*it] > priorities[toBePrinted]) {
                higherPriorityExist = true;
                break;
            }
        }

        if (higherPriorityExist) {
            q.push_back(toBePrinted);
        } else {
            printedCount += 1;
            if (toBePrinted == location) return printedCount;
        }
    }
}

int main() {
    // vector<int> priorities = { 2, 1, 3, 2 };
    // int location = 2;
    vector<int> priorities = { 1, 1, 9, 1, 1, 1 };
    int location = 0;

    cout << solution(priorities, location);

    return 0;
}