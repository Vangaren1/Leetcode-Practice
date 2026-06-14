// Best_Time_To_Buy_And_Sell_Stock_With_Cooldown.cpp
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
    struct PairHash
    {
        size_t operator()(const pair<int, int> &p) const
        {
            size_t h1 = hash<int>{}(p.first);
            size_t h2 = hash<int>{}(p.second);

            return h1 ^ (h2 << 1);
        }
    };

public:
    int maxProfit(vector<int> &prices)
    {
        unordered_map<pair<int, bool>, int, PairHash> cache;
        return rec(0, true, prices, cache);
    }
    int rec(int index, bool canBuy, vector<int> &prices, unordered_map<pair<int, bool>, int, PairHash> &c)
    {
        if (index >= prices.size())
        {
            return 0;
        }
        if (c.count({index, canBuy}))
        {
            return c[{index, canBuy}];
        }
        int cool = rec(index + 1, canBuy, prices, c);
        int buyOrSell;
        if (canBuy)
        {
            buyOrSell = rec(index + 1, !canBuy, prices, c) - prices[index];
        }
        else
        {
            buyOrSell = rec(index + 2, !canBuy, prices, c) + prices[index];
        }
        c[{index, canBuy}] = max(cool, buyOrSell);
        return c[{index, canBuy}];
    }
};
