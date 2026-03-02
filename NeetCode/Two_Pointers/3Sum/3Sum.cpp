// 3Sum.cpp
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
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        int n = nums.size();

        int left{0}, right{0}, currSum{0}, tmp{0};

        for (int index = 0; index < n - 2; index++)
        {
            if (index > 0 && nums[index] == nums[index - 1])
            {
                continue;
            }
            if (nums[index] > 0)
            {
                break;
            }

            left = index + 1;
            right = n - 1;

            while (left < right)
            {
                currSum = nums[index] + nums[left] + nums[right];

                if (currSum == 0)
                {
                    results.push_back({nums[index], nums[left], nums[right]});
                    tmp = nums[left];
                    while (left < right && nums[left] == tmp)
                        left++;
                    tmp = nums[right];
                    while (left < right && nums[right] == tmp)
                        right--;
                }
                else if (currSum < 0)
                {
                    tmp = nums[left];
                    while (left < right && nums[left] == tmp)
                        left++;
                }
                else if (currSum > 0)
                {
                    tmp = nums[right];
                    while (left < right && nums[right] == tmp)
                        right--;
                }
            }
        }
        return results;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {-1, 0, 1, 2, -1, -4};

    vector<vector<int>> r = sol.threeSum(nums);

    return 0;
}
