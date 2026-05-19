// Maximum_SubArray.cpp
//
// Compile locally with:
// clang++ Maximum_SubArray.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int maxSubArray(vector<int> &nums)
    {
        int maxSub = nums[0];
        int curSum(0);
        for (int n : nums)
        {
            if (curSum < 0)
            {
                curSum = 0;
            }
            curSum = curSum + n;
            maxSub = max(maxSub, curSum);
        }
        return maxSub;
    }
};

int main()
{
    cout << "Running Maximum_SubArray.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
