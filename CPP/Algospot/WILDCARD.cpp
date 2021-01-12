#include <iostream>
#include <string>

std::string text, regex;
bool match = true;

void solve(int regex_index, int text_index) {
    char regex_char = regex.at(regex_index);
    switch (regex_char)
    {
        case '*': {
            while (regex_index < regex.length()) {
                switch (regex.at(regex_index))
                {
                    case '*': {
                        regex_index++;
                    } break;

                    case '\0':
                        return;
                    
                    case '?': {

                    } break;

                    default: {

                    } break;
                }
            }
        } break;

        case '?':
            return solve(regex_index + 1, text_index + 1);

        case '\0':
            return;

        default: {
            
        } break;
    }
}

int main() {
    int N;
    std::cin >> N;
    for(int _ = 0; _ < N; _++) {
        std::cin >> regex;

        int test_cases;
        std::cin >> test_cases;

        for(int i = 0; i < test_cases; i++) {
            std::cin >> text;
            solve(0, 0);
        }
    }

    return 0;
}