#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef std::pair<int, std::pair<int, int>> timePair; // <index, <start, end>>

bool compare(timePair p1, timePair p2) {
    return p1.second.second < p2.second.second;
}

void solve() {
    int N;
    cin >> N;

    // vector<timePair> weeklyMeeting(N, timePair(0, pair<int, int>(0, 0)));
    // vector<timePair> monthlyMeeting(N, timePair(0, 0));
    vector<timePair> meetings(N * 2, pair<int, pair<int, int>>(0, pair<int,int>(0, 0)));
    vector<bool> meeting_record(N, false);

    for (int i = 0; i < N; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        // timePair week { a, b }, month { c, d };
        // weeklyMeeting.at(i) = week;
        // monthlyMeeting.at(i) = month;
        meetings.at(i) = timePair(i, pair<int, int>(a, b));
        meetings.at(i + N) = timePair(i, pair<int, int>(c, d));
    }

    // sort(weeklyMeeting.begin(), weeklyMeeting.end(), compare);
    // sort(monthlyMeeting.begin(), monthlyMeeting.end(), compare);
    sort(meetings.begin(), meetings.end(), compare);

    vector<timePair> records;

    int time_end = 0;
    for (int i = 0; i < meetings.size(); i++) {
        auto meet = meetings.at(i);
        bool isMeetingHappened = meeting_record.at(meet.first);
        if (!isMeetingHappened && meet.second.first >= time_end) { // 미팅 시작
            meeting_record.at(meet.first) = true;
            time_end = meet.second.second;
            records.push_back(meet);
        }
    }

    bool success = true;
    for (auto flag : meeting_record) {
        if (!flag) {
            success = false;
            break;
        }
    }

    if (success) {
        cout << "POSSIBLE" << "\n";

        for (auto timePair : records) {
            cout << timePair.second.first << " " << timePair.second.second << "\n";
        }
    } else {
        cout << "IMPOSSIBLE" << "\n";
    }
}

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
        solve();

    return 0;
}