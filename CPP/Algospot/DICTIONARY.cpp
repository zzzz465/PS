#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>


std::vector<std::vector<int>> adj;

void makeGraph(const std::vector<std::string>& words) {
    adj = std::vector<std::vector<int>>(26, std::vector<int>(26, 0));

    for (int j = 1; j < words.size(); j++) {
        int i = j - 1;
        int len = std::min(words[i].size(), words[j].size());

        for (int k = 0; k < len; k++) {
            if (words[i][k] != words[j][k]) {
                int a = words[i][k] - 'a';
                int b = words[j][k] - 'a';
                adj[a][b] = 1;
                break;
            }
        }
    }
}

std::vector<int> seen, order;
void dfs(int here) {
    seen[here] = 1;
    for (int there = 0; there < adj.size(); there++)
        if(adj[here][there] && !seen[there])
            dfs(there);
    
    order.push_back(here);
}

std::vector<int> topologicalSort() {
    int m = adj.size();
    seen = std::vector<int>(m, 0);
    order.clear();
    for (int i = 0; i < m; i++) if (!seen[i]) dfs(i);

    std::reverse(order.begin(), order.end());

    for(int i = 0; i < m; i++)
        for(int j = i + 1; j < m; j++)
            if(adj[order[j]][order[i]])
                return std::vector<int>();

    return order;
}

int main() {
    int T;
    std::cin >> T;

    std::vector<std::string> words;
    for (int i = 0; i < T; i++) {
        words.clear();
        int N; std::cin >> N;
        for (int j = 0; j < N; j++) {
            std::string text; std::cin >> text;
            words.push_back(text);
        }

        makeGraph(words);
        auto result = topologicalSort();
        if (result.size() > 0) {
            for (char c : result)
                std::cout << (char)(c + 'a');
            std::cout << "\n";
        } else {
            std::cout << "INVALID HYPOTHESIS" << "\n";
        }
    }

    return 0;
}