// Permutations_II.cpp
//
// Compile locally with:
// clang++ Permutations_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<vector<int>> permuteUnique(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());

        vector<vector<int>> results;
        vector<bool> used(nums.size(), false);
        vector<int> curr;
        dfs(curr, nums, used, results);
        return results;
    }

    void dfs(vector<int> &curr, vector<int> &nums, vector<bool> &used, vector<vector<int>> &results)
    {
        if (curr.size() == nums.size())
        {
            results.push_back(curr);
            return;
        }

        for (int index = 0; index < nums.size(); index++)
        {
            if (used[index])
            {
                continue;
            }

            if (index > 0 && nums[index] == nums[index - 1] and !used[index - 1])
            {
                continue;
            }

            used[index] = true;
            curr.push_back(nums[index]);
            dfs(curr, nums, used, results);
            curr.pop_back();
            used[index] = false;
        }
    }
};

int main()
{
    cout << "Running Permutations_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
