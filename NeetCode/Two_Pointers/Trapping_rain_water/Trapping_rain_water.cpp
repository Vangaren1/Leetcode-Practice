// Trapping_rain_water.cpp
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
    int trap(vector<int> &height)
    {
        int left{0}, total{0}, leftMax{0}, rightMax{0};
        int right = height.size() - 1;
        leftMax = height[left];
        rightMax = height[right];

        while (left < right)
        {

            if (height[left] < height[right])
            {
                left++;
                leftMax = max(leftMax, height[left]);
                total += leftMax - height[left];
            }
            else
            {
                right--;
                rightMax = max(rightMax, height[right]);
                total += rightMax - height[right];
            }
        }

        return total;
    }
};
