#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector< vector<int> > adj;
vector<string> graph[26][26];
vector<int> indegree, outdegree;

void makeGraph(const vector<string>& words) {
    for(int i = 0; i < 26; i++)
        for(int j = 0; j < 26; j++)
            graph[i][j] = vector<string>();

    adj = vector<vector<int>>(26, vector<int>(26, 0));

    indegree = outdegree = vector<int>(26, 0);

    for(auto word : words) {
        int frontIndex = word.front() - 'a';
        int backIndex = word.back() - 'a';
        
        indegree[frontIndex] += 1;
        outdegree[backIndex] += 1;
        adj[frontIndex][backIndex] += 1;
        graph[frontIndex][backIndex].push_back(word);
    }
}

void getEulerCircuit(int here, vector<int>& circuit) {
    for (int there = 0; there < 26; there++) {
        while(adj[here][there] > 0) {
            adj[here][there]--;
            getEulerCircuit(there, circuit);
        }
    }
    circuit.push_back(here);
}

vector<int> getEulerTrailOrCircuit() {
    vector<int> circuit;

    for (int i = 0; i < 26; i++) {
        if (outdegree[i] == indegree[i] + 1) { // 시작점 탐색
            getEulerCircuit(i, circuit);
            return circuit;
        }
    }

    for (int i = 0; i < 26; i++) {
        if (outdegree[i]) {
            getEulerCircuit(i, circuit);
            return circuit;
        }
    }

    return circuit;
}

bool checkEuler() {
    int plus1 = 0, minus1 = 0;
    for (int i = 0; i < 26; i++) {
        int delta = outdegree[i] - indegree[i];
        if (delta < -1 || delta > 1) return false;
        if (delta == 1) plus1++;
        if (delta == -1) minus1++;
    }

    return (plus1 == 1) && (minus1 == 1) || (plus1 == 0 && minus1 == 0);
}

string solve() {
    int N;
    cin >> N;

    vector<string> words;

    for (int i = 0; i < N; i++) {
        string word; cin >> word;
        words.push_back(word);
    }

    makeGraph(words);
    if (!checkEuler()) return "IMPOSSIBLE";

    vector<int> circuit = getEulerTrailOrCircuit();

    if (circuit.size() != words.size() + 1) return "IMPOSSIBLE"; // 오일러 서킷 or 트레일 에서 서킷을 거름
    reverse(circuit.begin(), circuit.end());
    string ret;
    for (int i = 1; i < circuit.size(); i++) {
        int a = circuit[i-1], b = circuit[i];
        if (ret.size()) ret += " ";
        ret += graph[a][b].back();
        graph[a][b].pop_back();
    }

    return ret;
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        cout << solve() << "\n";
    }

    return 0;
}