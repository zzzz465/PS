#include <iostream>

using namespace std;

int main() {
    string s;
    cin >> s;

    int total = 0;
    int value = 0;
    bool minus = false;

    for(int i = 0; i < s.size(); i++) {
        char c = s.at(i);
        switch (c) {
            case '+': {
                if (minus) {
                    total -= value;
                } else {
                    total += value;
                }
                value = 0;
            } break;

            case '-': {
                if (minus)
                    total -= value;
                else {
                    total += value;
                    minus = true;
                }

                value = 0;
            } break;

            default: {
                value *= 10;
                value += s.at(i) - '0';
            } break;
        }
    }

    if (minus)
        total -= value;
    else
        total += value;

    cout << total;

    return 0;
}