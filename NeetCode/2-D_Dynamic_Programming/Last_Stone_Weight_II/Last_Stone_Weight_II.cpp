// Last_Stone_Weight_II.cpp
//
// Compile locally with:
// clang++ Last_Stone_Weight_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    struct PairHash
    {
        size_t operator()(const pair<int, int> &p) const
        {
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };

    unordered_map<pair<int, int>, int, PairHash> memo;
    int stonesum;
    int target;

public:
    int lastStoneWeightII(vector<int> &stones)
    {
        memo.clear();
        stonesum = 0;
        for (auto stone : stones)
        {
            stonesum += stone;
        }
        target = (stonesum) / 2;
        return dfs(0, 0, stones);
    }
    int dfs(int index, int total, vector<int> &stones)
    {
        if (index >= stones.size() || total >= target)
        {
            return (target - (stonesum - target));
        }
        if (memo.count({index, total}))
        {
            return memo[{index, total}];
        }

        int take1 = dfs(index + 1, total + stones[index], stones);
        int donttake1 = dfs(index + 1, total, stones);
        memo[{index, total}] = min(take1, donttake1);
        return memo[{index, total}];
    }
};

int main()
{
    cout << "Running Last_Stone_Weight_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
