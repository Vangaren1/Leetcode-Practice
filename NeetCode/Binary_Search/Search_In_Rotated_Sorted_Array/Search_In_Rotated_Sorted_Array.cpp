// Search_In_Rotated_Sorted_Array.cpp
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
    int search(vector<int> &nums, int target)
    {
        int left{0}, mid{-1}, right = nums.size() - 1;

        while (left <= right)
        {
            mid = left + (right - left) / 2;
            // check if mid is the target
            if (nums[mid] == target)
            {
                return mid;
            }

            // check if left half is sorted
            if (nums[left] <= nums[mid])
            {
                // if sorted, check if target is in left half
                if (nums[left] <= target && target < nums[mid])
                {
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
            }
            // check if right half is sorted
            else if (nums[mid] < nums[right])
            {
                // if right half is sorted, is mid in here?
                if (nums[mid] < target && target <= nums[right])
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid + 1;
                }
            }
        }
        return -1;
    }
};
