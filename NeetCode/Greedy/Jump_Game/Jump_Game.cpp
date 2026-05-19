// Jump_Game.cpp
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
    bool canJump(vector<int> &nums)
    {
        int endgoal = nums.size() - 1;
        for (int index = endgoal - 1; index > -1; index--)
        {
            if (index + nums[index] >= endgoal)
            {
                endgoal = index;
            }
        }
        return endgoal == 0;
    }
};
