// Coin_Change_II.cpp
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
    int change(int amount, vector<int> &coins)
    {
        vector<int> dp(0, amount + 1);
        dp[0] = 1;

        for (int coin : coins)
        {
            for (int index = coin; index < amount + 1; index++)
            {
                dp[index] = dp[index] + dp[index - coin];
            }
        }
        return dp[amount];
    }
};
