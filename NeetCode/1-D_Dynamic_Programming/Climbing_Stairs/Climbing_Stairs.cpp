// Climbing_Stairs.cpp
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
    int climbStairs(int n)
    {
        vector<int> cache(n + 1, 0);

        cache[0] = 1;
        cache[1] = 2;
        if (n < 2)
        {
            return cache[n - 1];
        }

        for (int index = 3; index < n + 1; index++)
        {
            cache[index - 1] = cache[index - 2] + cache[index - 3];
        }

        return cache[n - 1];
    }
};
