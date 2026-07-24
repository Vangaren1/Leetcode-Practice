// Minimum_Size_Subarray_Sum.cpp
//
// Compile locally with:
// clang++ Minimum_Size_Subarray_Sum.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int minSubArrayLen(int target, vector<int> &nums)
    {
        int size = INT32_MAX;
        int curr(0), left(0), val(0);

        for (int index = 0; index < nums.size(); index++)
        {
            val = nums[index];
            curr += nums[index];
            while (curr >= target)
            {
                size = min(size, index - left + 1);
                curr = curr - nums[left];
                left++;
            }
        }
        if (size < INT32_MAX)
        {
            return size;
        }
        return 0;
    }
};

int main()
{
    cout << "Running Minimum_Size_Subarray_Sum.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
