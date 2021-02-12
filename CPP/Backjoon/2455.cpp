#include <iostream>
#include <vector>

using namespace std;

int main() {
    // vector<int> aboard;
    // vector<int> getoff;

    int count = 0;
    int max_count = 0;
    for (int i = 0; i < 4; i++) {
        int a, b;
        cin >> a >> b;
        count += (b - a);
        max_count = max(max_count, count);
    }

    cout << max_count << "\n";

    return 0;
}