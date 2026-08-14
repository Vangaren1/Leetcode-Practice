// Coin_Change.cpp
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
    int coinChange(vector<int> &coins, int amount)
    {
        vector<long long> dp(amount + 1, INT_MAX);
        dp[0] = 0;

        for (int amt = 1; amt < amount + 1; amt++)
        {
            for (auto coin : coins)
            {
                if (amt - coin >= 0)
                {
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1);
                }
            }
        }
        if (dp[amount] == INT32_MAX)
        {
            return -1;
        }
        return dp[amount];
    }
};
