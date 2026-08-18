// Minimum_Path_Sum.cpp
//
// Compile locally with:
// clang++ Minimum_Path_Sum.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int minPathSum(vector<vector<int>> &grid)
    {
        int height = grid.size();
        int width = grid[0].size();

        vector<vector<long>> dp(height + 1, vector<long>(width + 1, INT32_MAX));

        dp[height - 1][width - 1] = grid[height - 1][width - 1];
        for (int y = height - 1; y >= 0; y--)
        {
            for (int x = width - 1; x >= 0; x--)
            {
                if (y == height - 1 && x == width - 1)
                {
                    continue;
                }
                dp[y][x] = grid[y][x] + min(dp[y + 1][x], dp[y][x + 1]);
            }
        }
        return dp[0][0];
    }
};

int main()
{
    cout << "Running Minimum_Path_Sum.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
