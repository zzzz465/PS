#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

constexpr double pi = 3.14159265358979323846;

typedef long long ll;

int main() {
    int r;

    cin >> r;

    double euclidArea = r * r * pi;

    double non_euclidArea = r * r / 2 * 4;

    cout.precision(6);
    cout << fixed << euclidArea << "\n" << non_euclidArea;

    return 0;
}