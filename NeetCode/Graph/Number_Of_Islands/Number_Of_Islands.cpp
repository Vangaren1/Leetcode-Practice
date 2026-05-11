// Number_Of_Islands.cpp
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
    int numIslands(vector<vector<char>> &grid)
    {
        int height = grid.size();
        int width = grid[0].size();
        int count = 0;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] == '1')
                {
                    count++;
                    bfs({y, x}, grid);
                }
            }
        }
        return count;
    }

    void bfs(pair<int, int> xy, vector<vector<char>> &grid)
    {
        int height = grid.size();
        int width = grid[0].size();
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

        queue<pair<int, int>> q;
        q.push(xy);
        grid[xy.first][xy.second] = '#';

        while (!q.empty())
        {
            pair<int, int> tmp = q.front();
            q.pop();

            for (pair<int, int> dydx : directions)
            {
                int ny = tmp.first + dydx.first;
                int nx = tmp.second + dydx.second;
                pair<int, int> newTmp = {ny, nx};
                if (0 <= ny && ny < height &&
                    0 <= nx && nx < width &&
                    grid[ny][nx] == '1')
                {
                    grid[ny][nx] = '#';
                    q.push(newTmp);
                }
            }
        }
    }
};
