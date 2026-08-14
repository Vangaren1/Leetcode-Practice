// Integer_Break.cpp
//
// Compile locally with:
// clang++ Integer_Break.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int integerBreak(int n)
    {
        unordered_map<int, int> init = {
            {2, 1},
            {3, 2},
            {4, 4},
            {5, 6}};
        if (init.count(n))
        {
            return init[n];
        }
        vector<long long> dp(n + 1, 0);
        for (auto [key, val] : init)
        {
            dp[key] = val;
        }
        for (int i = 6; i < n + 1; i++)
        {
            if (i % 3 == 0)
            {
                dp[i] = 3 * dp[i - 1] / 2;
            }
            else if (i % 3 == 1)
            {
                dp[i] = 4 * dp[i - 1] / 3;
            }
            else
            {
                dp[i] = 2 * dp[i - 2];
            }
        }
        return dp[n];
    }
};

int main()
{
    cout << "Running Integer_Break.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
