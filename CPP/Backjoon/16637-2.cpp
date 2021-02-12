#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<char> input;

bool isNumber(char c) {
    return '0' <= c && c <= '9';
}

vector<char> postfix(const vector<char>& resource) {
    vector<char> result;
    stack<char> operators;
    for (auto c : resource) {
        if (isNumber(c)) {
            result.push_back(c);
        } else {
            if (c == '+' || c == '-' || c == '*') {
                if (operators.size() > 0 && operators.top() != '(') {
                    result.push_back(operators.top());
                    operators.pop();
                    operators.push(c);
                } else {
                    operators.push(c);
                }
            } else if (c == '(') {
                result.push_back(c);
            } else { // ')'
                result.push_back(operators.top());
                operators.pop(); // operator와 ( 를 뽑아냄
                operators.pop();
            }
        }
    }

    while (operators.size() > 0) {
        result.push_back(operators.top());
        operators.pop();
    }

    return result;
}

int getValue(const vector<char>& values) {
    stack<int> numbers;

    for (auto val : values) {
        if (isNumber(val)) {
            numbers.push(val - '0');
        } else {
            int val2, val1;
            val2 = numbers.top(); numbers.pop();
            val1 = numbers.top(); numbers.pop();

            int res;
            if (val == '+')
                res = val1 + val2;
            else if (val == '-')
                res = val1 - val2;
            else
                res = val1 * val2;

            numbers.push(res);
        }
    }

    return numbers.top();
}

void modify(vector<char> text, vector<char>::iterator it) {
    while (it != text.end()) {
        char c = *it;
        if (c == '+' || c == '-' || c == '*') {
            modify(text, it + 1);
            text.insert(it - 1, '(');
            text.insert(it + 2, ')');
            it += 3;
        } else {
            it += 1;
        }
    }

    auto postfixfied = postfix(text);
    cout << "li: ";
    for (auto c : postfixfied)
        cout << c << " ";
    cout << "\n";
    auto res = getValue(postfixfied);

    cout << "result: " << res << "\n";
}

void solve() {
    modify(input, input.begin());
}

int main() {
    int N; cin >> N;

    for (int i = 0; i < N; i++) {
        char val; cin >> val;
        input.push_back(val);
    }

    solve();

    return 0;
}