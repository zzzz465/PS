#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector< vector<int> > adj;
vector<int> sccId;
vector<int> discovered;
stack<int> st;
int sccCounter, vertexCounter;

/*
    here를 루트로 하는 서브트리에서 역방향 간선이나 교차 간선을 통해
    갈수있는 정점 중 **최소 발견 순서**를 반환한다.
    (이미 SCC로 묶인 정점으로 연결된 간선은 제외한다)
*/
int scc(int here) {
    int ret = discovered[here] = vertexCounter++;
    st.push(here);

    for (int i = 0; i < adj[here].size(); i++) {
        int there = adj[here][i];

        if (discovered[there] == -1) { // 트리 간선
            ret = min(ret, scc(there));
        } else if (sccId[there] == -1) { // 아직 연결된 곳이 scc로 묶이지 않았다면 -> 교차 간선?
            ret = min(ret, discovered[there]);
        }
    }

    // here 에서 부모로 올라가는 노드를 끊을까?
    if (ret == discovered[here]) { // 내가 최상위 노드네?
        while (true) {
            int t = st.top();
            st.pop();
            sccId[t] = sccCounter;
            if (t == here) break;
        }
        sccCounter++;
    }

    return ret;
}

vector<int> tarjanSCC() {
    sccId = discovered = vector<int>(adj.size(), -1);
    sccCounter = vertexCounter = 0;
    for (int i = 0; i < adj.size(); i++)
        if (discovered[i] == -1)
            scc(i);

    return sccId;
}
