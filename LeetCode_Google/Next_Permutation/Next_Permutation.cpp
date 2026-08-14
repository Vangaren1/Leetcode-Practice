// Next_Permutation.cpp
//
// Compile locally with:
// clang++ Next_Permutation.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    void nextPermutation(vector<int> &nums)
    {
        int n = nums.size();
        int left = n - 2;
        int right = n - 1;
        int tmp = 0;
        while (left >= 0 && nums[left] >= nums[left + 1])
        {
            left--;
        }
        if (left < 0)
        {
            left = 0;
            while (left < right)
            {
                tmp = nums[right];
                nums[right] = nums[left];
                nums[left] = tmp;
                left++;
                right--;
            }
            return;
        }

        right = left + 1;
        for (int index = right; index < n; index++)
        {
            if (nums[left] < nums[index])
            {
                right = index;
            }
        }
        tmp = nums[right];
        nums[right] = nums[left];
        nums[left] = tmp;

        left++;
        right = n - 1;
        while (left < right)
        {
            tmp = nums[right];
            nums[right] = nums[left];
            nums[left] = tmp;
            left++;
            right--;
        }
    }
};

int main()
{
    cout << "Running Next_Permutation.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
