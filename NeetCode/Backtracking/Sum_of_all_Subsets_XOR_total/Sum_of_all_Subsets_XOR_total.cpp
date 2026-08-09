// Sum_of_all_Subsets_XOR_total.cpp
//
// Compile locally with:
// clang++ Sum_of_all_Subsets_XOR_total.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int subsetXORSum(vector<int> &nums)
    {
        vector<int> curr;
        vector<vector<int>> results;
        int total(0), tmp(0);
        dfs(nums, curr, results, 0);

        for (auto &subset : results)
        {
            tmp = 0;
            for (auto &val : subset)
            {
                tmp = tmp ^ val;
            }
            total += tmp;
        }
        return total;
    }
    void dfs(vector<int> &nums, vector<int> &curr, vector<vector<int>> &results, int index)
    {
        if (index == nums.size())
        {
            results.push_back(curr);
            return;
        }

        curr.push_back(nums[index]);
        dfs(nums, curr, results, index + 1);

        curr.pop_back();
        dfs(nums, curr, results, index + 1);
    }
};

int main()
{
    cout << "Running Sum_of_all_Subsets_XOR_total.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
