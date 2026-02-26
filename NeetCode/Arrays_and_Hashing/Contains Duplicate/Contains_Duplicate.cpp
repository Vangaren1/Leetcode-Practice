// Contains_Duplicate.cpp
//
// Compile locally with:
// clang++ Contains_Duplicate.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool hasDuplicate(vector<int> &nums)
    {
        unordered_set<int> seen;

        for (int i = 0; i < nums.size(); i++)
        {
            auto result = seen.insert(nums[i]);
            if (!result.second)
            {
                return true;
            }
        }

        return false;
    }
};

int main()
{
    cout << "Running Contains_Duplicate.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
