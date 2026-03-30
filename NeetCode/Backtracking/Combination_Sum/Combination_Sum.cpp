// Combination_Sum.cpp
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
    vector<vector<int>> combinationSum(vector<int> &nums, int target)
    {
        vector<int> curr;
        vector<vector<int>> results;
        dfs(nums, target, curr, results, 0, 0);
        return results;
    }

    void dfs(vector<int> &nums, int target, vector<int> &curr, vector<vector<int>> &results, int index, int total)
    {
        if (total == target)
        {
            results.push_back(curr);
            return;
        }

        if (total > target || index >= nums.size())
        {
            return;
        }

        curr.push_back(nums[index]);
        dfs(nums, target, curr, results, index, total + nums[index]);
        curr.pop_back();
        dfs(nums, target, curr, results, index + 1, total);
    }
};
