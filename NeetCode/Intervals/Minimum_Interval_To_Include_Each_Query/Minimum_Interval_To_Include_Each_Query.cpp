// Minimum_Interval_To_Include_Each_Query.cpp
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
    vector<int> minInterval(vector<vector<int>> &intervals, vector<int> &queries)
    {
        unordered_map<int, int> intervalMap;

        for (const auto interval : intervals)
        {
            int currLen = interval[1] - interval[0] + 1;
            for (int i = interval[0]; i <= interval[1]; i++)
            {
                if (intervalMap.count(i))
                {
                    intervalMap[i] = min(currLen, intervalMap[i]);
                }
                else
                {
                    intervalMap[i] = currLen;
                }
            }
        }
        vector<int> results;
        for (const auto q : queries)
        {
            if (intervalMap.count(q))
            {
                results.push_back(intervalMap[q]);
            }
            else
            {
                results.push_back(-1);
            }
        }
        return results;
    }
};
