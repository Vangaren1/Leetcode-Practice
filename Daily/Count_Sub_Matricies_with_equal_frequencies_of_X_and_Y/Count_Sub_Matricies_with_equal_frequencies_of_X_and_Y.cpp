// Count_Sub_Matricies_with_equal_frequencies_of_X_and_Y.cpp
//
// Compile locally with:
// clang++ Count_Sub_Matricies_with_equal_frequencies_of_X_and_Y.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int numberOfSubmatrices(vector<vector<char>> &grid)
    {
        int height = grid.size();
        int width = grid[0].size();
        int count{0};
        vector<vector<pair<int, int>>> dp(height + 1, vector<pair<int, int>>(width + 1, {0, 0}));

        for (int y = 1; y < height + 1; y++)
        {
            for (int x = 1; x < width + 1; x++)
            {
                char cell = grid[y - 1][x - 1];
                dp[y][x].first = dp[y - 1][x].first + dp[y][x - 1].first - dp[y - 1][x - 1].first;
                dp[y][x].second = dp[y - 1][x].second + dp[y][x - 1].second - dp[y - 1][x - 1].second;

                if (cell == 'X')
                {
                    dp[y][x].first++;
                }
                else if (cell == 'Y')
                {
                    dp[y][x].second++;
                }

                if (dp[y][x].first && dp[y][x].first == dp[y][x].second)
                {
                    count++;
                }
            }
        }
        return count;
    }
};

int main()
{
    cout << "Running Count_Sub_Matricies_with_equal_frequencies_of_X_and_Y.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
