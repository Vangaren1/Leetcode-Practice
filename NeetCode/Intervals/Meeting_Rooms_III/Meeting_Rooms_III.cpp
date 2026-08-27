// Meeting_Rooms_III.cpp
//
// Compile locally with:
// clang++ Meeting_Rooms_III.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
//
// NOTE:
// - Remove main() before submitting to LeetCode.
// - Keep only the class Solution definition.
//

#include <algorithm>
#include <array>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

class Solution
{
public:
    int mostBooked(int n, vector<vector<int>> &meetings)
    {
        sort(meetings.begin(), meetings.end());
        vector<int> roomCount(n, 0);
        priority_queue<int, vector<int>, greater<int>> available;
        priority_queue<pair<long, int>, vector<pair<long, int>>, greater<pair<long, int>>> occupied;

        for (int i = 0; i < n; i++)
        {
            available.push(i);
        }

        int freeTime(0), room(0);
        for (const auto &meeting : meetings)
        {
            int start = meeting[0];
            int end = meeting[1];
            int duration = end - start;
            while (!occupied.empty() && occupied.top().first <= start)
            {
                auto [freeTime, tmproom1] = occupied.top();
                room = tmproom1;
                occupied.pop();
                available.push(room);
            }

            if (!available.empty())
            {
                room = available.top();
                available.pop();
                occupied.push({end, room});
            }
            else
            {
                auto [freeTime, tmpRoom2] = occupied.top();
                occupied.pop();
                room = tmpRoom2;
                occupied.push({freeTime + duration, room});
            }
            roomCount[room] += 1;
        }
        return max_element(roomCount.begin(), roomCount.end()) - roomCount.begin();
    }
};

int main()
{
    cout << "Running Meeting_Rooms_III.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
