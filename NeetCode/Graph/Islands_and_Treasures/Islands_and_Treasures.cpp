// Islands_and_Treasures.cpp
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
    void islandsAndTreasure(vector<vector<int>> &grid)
    {
        vector<pair<int, int>> diff = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int height = grid.size();
        int width = grid[0].size();
        int inf = INT32_MAX;

        deque<pair<int, int>> q;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] == 0)
                {
                    q.push_back({y, x});
                }
            }
        }

        while (!q.empty())
        {
            pair<int, int> curr = q.front();
            q.pop_front();

            int cy = curr.first;
            int cx = curr.second;
            for (pair<int, int> dyx : diff)
            {
                int ny = cy + dyx.first;
                int nx = cx + dyx.second;
                if (0 <= ny && ny < height && 0 <= nx && nx < width && grid[ny][nx] == inf)
                {
                    grid[ny][nx] = grid[cy][cx] + 1;
                    q.push_back({ny, nx});
                }
            }
        }
    }
};
