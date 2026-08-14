// Combination_Sum_IV.cpp
//
// Compile locally with:
// clang++ Combination_Sum_IV.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    unordered_map<int, int> memo;

public:
    int combinationSum4(vector<int> &nums, int target)
    {
        memo.clear();
        sort(nums.begin(), nums.end());
        return dfs(0, target, nums);
    }
    int dfs(int total, int target, vector<int> &nums)
    {
        if (memo.count(total))
        {
            return memo[total];
        }
        if (total == target)
        {
            return 1;
        }
        int count = 0;
        for (auto num : nums)
        {
            if (total + num > target)
            {
                break;
            }
            count += dfs(total + num, target, nums);
        }
        memo[total] = count;
        return count;
    }
};

int main()
{
    cout << "Running Combination_Sum_IV.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
