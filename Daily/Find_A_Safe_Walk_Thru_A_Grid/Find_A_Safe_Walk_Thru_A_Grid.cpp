// Find_A_Safe_Walk_Thru_A_Grid.cpp
//
// Compile locally with:
// clang++ Find_A_Safe_Walk_Thru_A_Grid.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool findSafeWalk(vector<vector<int>> &grid, int health)
    {
        int height = grid.size();
        int width = grid[0].size();
        vector<vector<int>> dist(height, vector<int>(width, INT32_MAX));
        dist[0][0] = grid[0][0];
        deque<pair<int, int>> dq;
        dq.push_back({0, 0});
        vector<pair<int, int>> diff = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int ny, nx, cost, totalCost(0);
        while (!dq.empty())
        {
            auto [y, x] = dq.front();
            dq.pop_front();
            for (auto [dy, dx] : diff)
            {
                ny = dy + y;
                nx = dx + x;
                if (ny < 0 || ny >= height || nx < 0 || nx >= width)
                {
                    continue;
                }
                cost = grid[ny][nx];
                totalCost = dist[y][x] + cost;
                if (totalCost > health)
                {
                    continue;
                }

                if (totalCost < dist[ny][nx])
                {
                    dist[ny][nx] = totalCost;
                    if (cost == 0)
                    {
                        dq.push_front({ny, nx});
                    }
                    else
                    {
                        dq.push_back({ny, nx});
                    }
                }
            }
        }
        return dist[height - 1][width - 1] < health;
    }
};

int main()
{
    cout << "Running Find_A_Safe_Walk_Thru_A_Grid.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
