// First_Missing_Positive.cpp
//
// Compile locally with:
// clang++ First_Missing_Positive.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int firstMissingPositive(vector<int> &nums)
    {
        int n = nums.size();
        for (int index = 0; index < n; index++)
        {
            if (nums[index] <= 0 || nums[index] > n)
            {
                nums[index] = 0;
                continue;
            }
            hop(nums[index], nums);
        }
        for (int idx = 0; idx < n; idx++)
        {
            if (nums[idx] != idx + 1)
            {
                return idx + 1;
            }
        }
        return n + 1;
    }
    void hop(int value, vector<int> &nums)
    {
        while (nums[value - 1] != value)
        {
            int curr = nums[value - 1];
            nums[value - 1] = value;
            if (curr <= 0 || curr > nums.size())
            {
                break;
            }
            value = curr;
        }
    }
};

int main()
{
    cout << "Running First_Missing_Positive.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
