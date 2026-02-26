// longest_consecutive_sequence.cpp
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
    int longestConsecutive(vector<int> &nums)
    {
        int best = 0;
        unordered_set<int> values(nums.begin(), nums.end());

        for (int val : values)
        {
            if (values.count(val - 1) > 0)
            {
                continue;
            }
            int nxt = val;
            while (values.count(nxt) > 0)
            {
                nxt += 1;
            }
            best = max(best, nxt - val);
        }
        return best;
    }
};