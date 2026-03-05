// Best_Time_To_Buy_and_Sell_Stock.cpp
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
    int maxProfit(vector<int> &prices)
    {
        int minSell = prices[0];
        int maxProfit{0}, curr{0};

        for (int num : prices)
        {
            curr = num - minSell;
            maxProfit = max(maxProfit, curr);
            minSell = min(minSell, num);
        }
        return maxProfit;
    }
};
