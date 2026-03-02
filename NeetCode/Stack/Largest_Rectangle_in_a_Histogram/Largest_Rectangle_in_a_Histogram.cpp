// Largest_Rectangle_in_a_Histogram.cpp
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
    int largestRectangleArea(vector<int> &heights)
    {
        int maxArea = 0;
        vector<pair<int, int>> stack;
        int height = 0;
        int start = 0;
        int idx = 0;
        int h = 0;
        for (int index = 0; index < heights.size(); index++)
        {
            height = heights[index];
            start = index;

            while (!stack.empty() && stack.back().second > height)
            {
                idx = stack.back().first;
                h = stack.back().second;
                stack.pop_back();
                maxArea = max(maxArea, h * (index - idx));
                start = idx;
            }

            stack.push_back({start, height});
        }

        // if the stack isn't empty after iterating thru, iterate thru the stack

        for (pair<int, int> tmp : stack)
        {
            idx = tmp.first;
            height = tmp.second;
            maxArea = max(maxArea, (int)(height * (heights.size() - idx)));
        }

        return maxArea;
    }
};
