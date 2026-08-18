// Unique_Paths_II.cpp
//
// Compile locally with:
// clang++ Unique_Paths_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid)
    {
        int height = obstacleGrid.size();
        int width = obstacleGrid[0].size();
        vector<vector<long>> dp(height + 1, vector<long>(width + 1, 0));
        if (obstacleGrid[height - 1][width - 1] == 0)
        {
            dp[height - 1][width - 1] = 1;
        }

        for (int y = height - 1; y >= 0; y--)
        {
            for (int x = width - 1; x >= 0; x--)
            {
                if (obstacleGrid[y][x] == 1)
                {
                    continue;
                }
                dp[y][x] += dp[y + 1][x] + dp[y][x + 1];
            }
        }
        return dp[0][0];
    }
};

int main()
{
    cout << "Running Unique_Paths_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
