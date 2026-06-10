// Burst_Balloons.cpp
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
    int maxCoins(vector<int> &nums)
    {
        vector<vector<int>> dp(nums.size() + 2, vector<int>(nums.size() + 2, -1));
        vector<int> nnums = {1};
        nnums.insert(nnums.end(), nums.begin(), nums.end());
        nnums.push_back(1);

        return dfs(1, nums.size(), nnums, dp);
    }
    int dfs(int left, int right, vector<int> &nums, vector<vector<int>> &dp)
    {
        if (left > right)
        {
            return 0;
        }
        if (dp[left][right] != -1)
        {
            return dp[left][right];
        }
        dp[left][right] = 0;
        for (int i = left; i < right + 1; i++)
        {
            int coins = nums[i] * nums[right + 1] * nums[left - 1];
            coins += dfs(left, i - 1, nums, dp) + dfs(i + 1, right, nums, dp);
            dp[left][right] = max(dp[left][right], coins);
        }
        return dp[left][right];
    }
};
