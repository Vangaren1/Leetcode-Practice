// Contains_Duplicate_II.cpp
//
// Compile locally with:
// clang++ Contains_Duplicate_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool containsNearbyDuplicate(vector<int> &nums, int k)
    {
        unordered_map<int, int> curr;
        int val(0);
        for (int index = 0; index < nums.size(); index++)
        {
            val = nums[index];
            if (curr.count(val) && abs(index - curr[val]) <= k)
            {
                return true;
            }
            curr[val] = index;
        }
        return false;
    }
};

int main()
{
    cout << "Running Contains_Duplicate_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
