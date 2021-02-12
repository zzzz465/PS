#include <iostream>
#include <stack>
#include <string>

std::stack<char> stack;

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++) {
        std::string s;
        std::cin >> s;

        while (stack.size() > 0) stack.pop(); // clear stack

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{')
                stack.push(c);

            if (c == ')' || c == ']' || c == '}') {
                if (stack.size() > 0) {
                    char top = stack.top();
                    if (c == ')' && top != '(')
                        break;
                    else if (c == ']' && top != '[')
                        break;
                    else if (c == '}' && top != '{')
                        break;

                    stack.pop();
                } else {
                    stack.push('X'); // 에러
                    break;
                }
            }
        }
        
        if (stack.size() == 0)
            std::cout << "YES";

        else
            std::cout << "NO";

        std::cout << "\n";
    }

    return 0;
}