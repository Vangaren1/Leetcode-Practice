// Sliding_Window_Maximum.cpp
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
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        priority_queue<pair<int, int>> maxQ;
        vector<int> results;

        int left{0};
        int n = nums.size();

        for (int right = 0; right < n; right++)
        {

            maxQ.push({nums[right], right});
            left = right - k + 1;

            if (left >= 0)
            {

                while (maxQ.top().second < left)
                {
                    maxQ.pop();
                }
                results.push_back(maxQ.top().first);
            }
        }

        return results;
    }
};
