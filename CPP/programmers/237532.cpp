#include <iostream>
#include <string>
#include <vector>
#include <climits>

using namespace std;

string solution(string s) {
    int min_val = INT_MAX;
    int max_val = INT_MIN;

    string temp;
    for(auto c : s) {
        if (c != ' ')
            temp.push_back(c);
        else {
            int value = stoi(temp);
            min_val = min(min_val, value);
            max_val = max(max_val, value);
            temp.clear();
        }
    }

    
    int value = stoi(temp);
    min_val = min(min_val, value);
    max_val = max(max_val, value);
    temp.clear();

    string result;
    result.append(to_string(min_val));
    result.append(" ");
    result.append(to_string(max_val));

    return result;
}

int main() {


    return 0;
}