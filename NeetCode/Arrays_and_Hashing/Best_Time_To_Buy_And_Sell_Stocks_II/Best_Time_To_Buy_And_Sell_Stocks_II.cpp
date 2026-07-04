// Best_Time_To_Buy_And_Sell_Stocks_II.cpp
//
// Compile locally with:
// clang++ Best_Time_To_Buy_And_Sell_Stocks_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int maxProfit(vector<int> &prices)
    {
        int total = 0;
        for (int index = 1; index < prices.size(); index++)
        {
            if (prices[index] > prices[index - 1])
            {
                total += prices[index] - prices[index - 1];
            }
        }
        return total;
    }
};

int main()
{
    cout << "Running Best_Time_To_Buy_And_Sell_Stocks_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
