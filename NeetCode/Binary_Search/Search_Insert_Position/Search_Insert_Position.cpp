// Search_Insert_Position.cpp
//
// Compile locally with:
// clang++ Search_Insert_Position.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int searchInsert(vector<int> &nums, int target)
    {
        if (nums[0] < target)
        {
            return 0;
        }
        if (nums.back() > target)
        {
            return nums.size();
        }
        int left(0), mid(0);
        int right = nums.size() - 1;
        while (left <= right)
        {
            mid = (left + right) / 2;
            if (nums[mid] == target)
            {
                return mid;
            }
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        return left;
    }
};

int main()
{
    cout << "Running Search_Insert_Position.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
