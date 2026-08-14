// Absolute_Minimum_Effort.cpp
//
// Compile locally with:
// clang++ Absolute_Minimum_Effort.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int minimumEffortPath(vector<vector<int>> &heights)
    {
        int height(heights.size()), width(heights[0].size());
        vector<pair<int, int>> diff = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> dist(height, vector<int>(width, INT32_MAX));
        dist[0][0] = 0;
        priority_queue<
            pair<int, pair<int, int>>,
            vector<pair<int, pair<int, int>>>,
            greater<pair<int, pair<int, int>>>>
            pq;
        pq.push({0, {0, 0}});
        while (!pq.empty())
        {
            auto [effort, pos] = pq.top();
            auto [y, x] = pos;
            if (effort > dist[y][x])
            {
                continue;
            }
            if (y == height - 1 && x == width - 1)
            {
                return effort;
            }

            int curr = heights[y][x];
            for (auto [dy, dx] : diff)
            {
                int ny = y + dy;
                int nx = x + dx;

                if (0 <= ny && 0 <= nx && ny < height && nx < width)
                {
                    int newHeight = heights[ny][nx];
                    int stepDiff = abs(curr - newHeight);
                    int newEffort = max(effort, stepDiff);
                    if (newEffort < dist[ny][nx])
                    {
                        dist[ny][nx] = newEffort;
                        pq.push({newEffort, {ny, nx}});
                    }
                }
            }
        }
        return dist[height - 1][width - 1];
    }
};

int main()
{
    cout << "Running Absolute_Minimum_Effort.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
