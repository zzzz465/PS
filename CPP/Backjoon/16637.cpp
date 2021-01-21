#include <iostream>
#include <vector>
#include <stack>
#include <climits>

using namespace std;

vector<char> originalInput;

int max_val = INT_MIN;

bool isNumber(char c) {
    return '0' <= c && c <= '9';
}

void getMaxValue(const vector<char>& input) {
    stack<char> operators;

    vector<char> result;

    for (auto i : input) {
        if (isNumber(i)) {
            result.push_back(i);
        } else {
            switch (i) {
                case '(': {
                    operators.push(i);
                } break;

                case ')': {
                    while (true) {
                        auto top = operators.top();
                        operators.pop();
                        if (top == '(') {
                            break;
                        } else {
                            result.push_back(top);
                        }
                    }
                } break;

                case '+':
                case '-':
                case '*': {
                    operators.push(i);
                } break;
            }
        }
    }

    while (operators.size() > 0) {
        auto top = operators.top();
        result.push_back(top);
        operators.pop();
    }

    cout << "input: ";
    for (auto i : input)
        cout << i << " ";
    cout << "\n";

    stack<int> numbers;

    for (auto c : result) {
        if (isNumber(c)) {
            numbers.push(c - '0');
        } else {
            int val2 = numbers.top();
            numbers.pop();
            int val1 = numbers.top();
            numbers.pop();

            int res;
            switch (c) {
                case '+':
                    res = val1 + val2;
                    break;

                case '-':
                    res = val1 - val2;
                    break;

                case '*':
                    res = val1 * val2;
                    break;
            }

            numbers.push(res);
        }
    }

    cout << "result: " << numbers.top() << "\n";
    max_val = max(numbers.top(), max_val);
}

void recursive(vector<char> input, int index) {
    while (index < input.size()) {
        if (input[index] == '*' || input[index] == '+' || input[index] == '-') {
            recursive(input, index + 1);
            input.insert(input.begin() + index - 1, '(');
            input.insert(input.begin() + index + 3, ')'); // 2는 위에서 뭐 하나 집어넣었기 때문에
            recursive(input, index + 4);
            index += 4;
        } else {
            index += 1;
        }
    }

    getMaxValue(input);
}

void solve() {
    getMaxValue(originalInput); // 아무것도 안하고
    recursive(originalInput, 0);
    /*
    for (int i = 0; i < originalInput.size() - 1; i++) {
        for (int j = i + 1; j < originalInput.size() + 1; j++) {
            if (isNumber(originalInput[i]) && isNumber(originalInput[j-1])) { // operator 뒷쪽에 넣으면 비정상적인 입력으로 변함
                vector<char> replica = originalInput;
                replica.insert(replica.begin() + i, '(');
                replica.insert(replica.begin() + j + 1, ')');
                getMaxValue(replica);
            }
        }
    }
    */
}

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        char val; cin >> val;
        originalInput.push_back(val);
    }

    solve();

    return 0;
}