// Container_with_most_water.cpp
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
    int maxArea(vector<int> &heights)
    {
        int left{0}, maxSeen{0}, curr{0}, lVal{0}, rVal{0};
        int right = heights.size() - 1;

        while (left < right)
        {
            lVal = heights[left];
            rVal = heights[right];
            curr = (right - left) * min(lVal, rVal);
            maxSeen = max(maxSeen, curr);

            if (lVal <= rVal)
            {
                left++;
            }
            else
            {
                right--;
            }
        }
        return maxSeen;
    }
};
