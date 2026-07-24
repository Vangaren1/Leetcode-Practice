// Split_Array_Largest_Sum.cpp
//
// Compile locally with:
// clang++ Split_Array_Largest_Sum.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int splitArray(vector<int> &nums, int k)
    {
        int left(0), right(0), mid(0), pieces(0), curr(0);
        for (auto &num : nums)
        {
            left = max(left, num);
            right += num;
        }

        while (left <= right)
        {
            mid = left + (right - left) / 2;

            pieces = 1;
            curr = 0;
            for (auto &tmp : nums)
            {
                if (tmp + curr > mid)
                {
                    pieces++;
                    curr = tmp;
                }
                else
                {
                    curr += tmp;
                }
            }

            if (pieces <= k)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        return left;
    }
};

int main()
{
    cout << "Running Split_Array_Largest_Sum.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
