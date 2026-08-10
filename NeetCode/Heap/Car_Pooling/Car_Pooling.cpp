// Car_Pooling.cpp
//
// Compile locally with:
// clang++ Car_Pooling.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool carPooling(vector<vector<int>> &trips, int capacity)
    {
        sort(trips.begin(), trips.end(),
             [](const auto &a, const auto &b)
             { return a[1] < b[1]; });
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> hq;

        for (const auto &trip : trips)
        {
            int passenger = trip[0];
            int origin = trip[1];
            int destination = trip[2];

            while (!hq.empty() && hq.top().first <= origin)
            {
                pair<int, int> tmp = hq.top();
                hq.pop();
                capacity += tmp.second;
            }
            capacity = capacity - passenger;
            if (capacity < 0)
            {
                return false;
            }
            hq.push({destination, passenger});
        }
        return true;
    }
};

int main()
{
    cout << "Running Car_Pooling.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
