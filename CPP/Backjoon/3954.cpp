#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <stack>

using namespace std;

typedef unsigned char uchar;

string input;
int inputIndex;

char getInput() {
    return inputIndex < input.size() ? input.at(inputIndex++) : 255;
}

const int infinite_limit = 50000000;

string loop(vector<uchar>& memory, const unordered_map<int, int>& jump_table, const string code) {
    cout << "code: ";
    for (char c : code)
        cout << c << " ";
    cout << "\n";

    int pointer = 0;
    int pc = 0;
    int run_count = 0;
    stack<int> jump_stack;

    while (run_count < infinite_limit && pc < code.size()) {
        char opcode = code[pc];

        switch (opcode) {
            case '+': {
                memory[pointer] += 1;
            } break;

            case '-': {
                memory[pointer] -= 1;
            } break;

            case '<': {
                pointer = (pointer - 1) % memory.size();
            } break;

            case '>': {
                pointer = (pointer + 1) % memory.size();
            } break;

            case '[': {
                if (memory[pointer] == 0) {
                    pc = jump_table.at(pc);
                } else {
                    pc += 1;
                }
            } break;

            case ']': {
                if (memory[pointer] != 0) {
                    jump_stack.push(pc);
                    pc = jump_table.at(pc);
                } else {
                    jump_stack.pop();
                    pc += 1;
                }
            } break;

            case '.': {
                // 출력하는건데, 필요없다고 했음
            } break;

            case ',': {
                memory[pointer] = getInput(); // 이게 무한루프에 빠지면 어떻게 되는거냐???
            } break;
        }

        switch (opcode) {
            case '+':
            case '-':
            case '<':
            case '>':
            case '.':
            case ',':
                pc += 1;
                break;
        }

        run_count += 1;
    }

    if (run_count >= infinite_limit && pc < code.size()) {
        auto size = jump_stack.size();
        auto endIndex = jump_stack.top();
        auto startIndex = jump_table.at(endIndex) - 1;
        string result("Loops");
        result.append(" "); result.append(to_string(startIndex));
        result.append(" "); result.append(to_string(endIndex));

        return result;
        /*
        for (auto it = code.begin() + pc; it != code.end(); it++) {
            if (*it == '[') {
                jump_stack.push(-1);
            } else if (*it == ']') {
                int EndIndex = it - code.begin();

                if (jump_stack.size() > 1) {
                    jump_stack.pop();
                } else if (jump_stack.size() == 1) { // 문제의 지점
                    int startIndex = jump_table.at(EndIndex) - 1;
                    string result("Loops");
                    result.append(" "); result.append(to_string(startIndex));
                    result.append(" "); result.append(to_string(EndIndex));

                    return result;
                } else { // size = 0?
                    // 불가능???
                }
            }
        }
        // 여기 안오겠지?
        return "ERR";
        */
    }
    else {
        return "Terminates";
    }
}

void create_jump_table(unordered_map<int, int>& jump_table, const string code) {
    stack<int> s;

    for (int i = 0; i < code.size(); i++) {
        char opcode = code[i];

        if (opcode == '[') {
            s.push(i);
        } else if (opcode == ']') {
            int top = s.top();
            s.pop();
            jump_table[i] = top + 1;
            jump_table[top] = i + 1;
        }
    }
}

void run() {
    int memLen, codeLen, inputLen;
    cin >> memLen >> codeLen >> inputLen;

    vector<uchar> memory(memLen, 0);
    string code;
    unordered_map<int, int> jump_table;

    cin >> code;

    create_jump_table(jump_table, code);

    cin >> input;
    inputIndex = 0;

    cout << loop(memory, jump_table, code) << "\n";
}

int main() {
    int T; cin >> T;

    for (int i = 0; i < T; i++)
        run();

    return 0;
}