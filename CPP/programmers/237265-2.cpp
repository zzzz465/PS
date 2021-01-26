#include <string>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

typedef pair<int, int> Pos; // 위치, truck_index

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    sort(truck_weights.begin(), truck_weights.end());

    int bridge_weight_sum = 0;
    deque<Pos> trucks_on_bridge;

    int time = 0;

    while (truck_weights.size() > 0 || trucks_on_bridge.size() > 0) {
        bool advanced = false;
        if (truck_weights.size() > 0) {
            int back = truck_weights.back();
            if (back + bridge_weight_sum <= weight) {
                bridge_weight_sum += back;
                Pos pos;
                pos.second = back;
                trucks_on_bridge.push_back(pos);
                for (auto& truck : trucks_on_bridge)
                    truck.first += 1;
                time += 1;
                advanced = true;
                truck_weights.pop_back();
            }
        }

        if (!advanced) {
            auto front = trucks_on_bridge.front();
            auto timeAdd = bridge_length - front.first;
            for (auto& truck : trucks_on_bridge)
                truck.first += timeAdd;
            time += timeAdd;
        }

        while (trucks_on_bridge.size() > 0) {
            auto front = trucks_on_bridge.front();
            if (front.first == bridge_length) {
                trucks_on_bridge.pop_front();
                bridge_weight_sum -= front.second;
            } else {
                break;
            }
        }

    }

    return time + 1;
}

int main() {
    int bridge_length = 100;
    int weight = 100;
    vector<int> truck_weights{ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 };

    int result = solution(bridge_length, weight, truck_weights);

    return 0;
}