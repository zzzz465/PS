#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>

using namespace std;

bool isOperator(char c) {
    return c == '+' || c == '-';
}

int solve(const string& input) {
    // cout << "result: " << input << "\n";
    int left, left_end, opcodeIndex, right, right_end;
    if (input.front() == '(') {
        auto end = find(input.begin(), input.end(), ')');
        string left_str = string(input.begin() + 1, input.end() - 1);
        left = solve(left_str);
    } else {
        int left_end = 0;
        for (int i = 0; i < input.size(); i++) {
            if (isOperator(input.at(i)) || i == input.size() - 1) {
                left_end = i;
                break;
            }
        }

        left = stoi(string(input.begin(), input.begin() + left_end));
    }

    opcodeIndex = find_if(input.begin(), input.end(), isOperator) - input.begin();
    char opCode = input.at(opcodeIndex);
    int right_start = opcodeIndex + 1;
    if (input.at(right_start) == '(') {

    } else {
        
    }
}

void bracket(string input, int index) {

    for (int start = index; start < input.size(); start++) {
        if (start != 0 && !isOperator(input.at(start - 1))) // (숫자 <-- ( 에 해당하지 않으면 건너뜀
            continue;

        int operatorIndex = find_if(input.begin() + start, input.end(), isOperator) - input.begin();
        if (operatorIndex < input.size()) { // 괄호 가능, 찾았음
            for (int end = operatorIndex + 1; end <= input.size(); end++) {
                if (end == input.size() || isOperator(input.at(end))) {
                    string copy = input;
                    copy.insert(copy.begin() + end, ')');
                    copy.insert(copy.begin() + start, '(');
                    bracket(copy, end + 3); // (으로 밀려서 +1, ) 때문에 +1, operator 때문에 +1
                }
            }
        } else { // 못찾음

        }
    }

    solve(input);
}

int main() {
    string input;
    cin >> input;

    bracket(input, 0);

    return 0;
}