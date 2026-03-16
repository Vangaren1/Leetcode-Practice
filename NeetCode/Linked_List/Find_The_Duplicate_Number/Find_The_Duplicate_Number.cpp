// Find_The_Duplicate_Number.cpp
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
    int findDuplicate(vector<int> &nums)
    {
        for (int index = 0; index < nums.size(); index++)
        {
            int curr = nums[index];
            if (curr < 0)
            {
                return curr;
            }
            nums[abs(curr) - 1] *= 1;
        }

        return 0;
    }
};
