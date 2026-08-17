// Stone_Game_II.cpp
//
// Compile locally with:
// clang++ Stone_Game_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
private:
    int n;
    vector<vector<vector<int>>> dp;

public:
    int stoneGameII(vector<int> &piles)
    {
        n = piles.size();
        dp.clear();
        dp.resize(2, vector<vector<int>>(n, vector<int>(n + 1, -1)));
        return dfs(1, 0, 1, piles);
    }
    int dfs(int alice, int index, int m, vector<int> &piles)
    {
        if (index == piles.size())
        {
            return 0;
        }
        if (dp[alice][index][m] != -1)
        {
            return dp[alice][index][m];
        }
        int res = alice == 1 ? 0 : INT32_MAX;
        int total = 0;

        for (int x = 1; x <= 2 * m; x++)
        {
            if (index + x > piles.size())
                break;
            total += piles[index + x - 1];
            if (alice)
            {
                res = max(res, total + dfs(0, index + x, max(m, x), piles));
            }
            else
            {
                res = min(res, dfs(1, index + x, max(m, x), piles));
            }
        }
        dp[alice][index][m] = res;
        return res;
    }
};

int main()
{
    cout << "Running Stone_Game_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
