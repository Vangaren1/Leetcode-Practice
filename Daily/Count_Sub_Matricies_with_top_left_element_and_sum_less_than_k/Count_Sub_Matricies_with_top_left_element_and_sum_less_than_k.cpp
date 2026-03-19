// Count_Sub_Matricies_with_top_left_element_and_sum_less_than_k.cpp
//
// Compile locally with:
// clang++ Count_Sub_Matricies_with_top_left_element_and_sum_less_than_k.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int countSubmatrices(vector<vector<int>> &grid, int k)
    {
        int height = grid.size();
        int width = grid[0].size();
        int count{0};
        vector<vector<int>> dp(height + 1, vector<int>(width + 1, 0));

        for (int y = 1; y < height + 1; y++)
        {
            for (int x = 1; x < width + 1; x++)
            {
                dp[y][x] = grid[y - 1][x - 1] + dp[y - 1][x] + dp[y][x - 1] - dp[y - 1][x - 1];
                if (dp[y][x] <= k)
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
    cout << "Running Count_Sub_Matricies_with_top_left_element_and_sum_less_than_k.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
