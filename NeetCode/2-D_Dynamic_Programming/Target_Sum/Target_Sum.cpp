// Target_Sum.cpp
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
    int findTargetSumWays(vector<int> &nums, int target)
    {
        unordered_map<pair<int, int>, int, PairHash> cache;
        return dfs(0, 0, target, nums, cache);
    }
    int dfs(int index, int total, int target, vector<int> &nums, unordered_map<pair<int, int>, int, PairHash> &c)
    {
        if (index == nums.size())
        {
            if (total == target)
            {
                return 1;
            }
            return 0;
        }
        if (c.count({index, total}))
        {
            return c[{index, total}];
        }

        int curr = nums[index];
        c[{index, total}] = dfs(index + 1, total - curr, target, nums, c) + dfs(index + 1, total + curr, target, nums, c);
        return c[{index, total}];
    }
};
