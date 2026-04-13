// Min_Cost_Climbing_Stairs.cpp
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
    int minCostClimbingStairs(vector<int> &cost)
    {
        vector<int> paid(cost);

        paid.push_back(0);

        for (int index = paid.size() - 3; index > -1; index--)
        {
            paid[index] = paid[index] + min(paid[index + 1], paid[index + 2]);
        }

        return min(paid[0], paid[1]);
    }
};
