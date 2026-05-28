// Reverse_Integer.cpp
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
    int reverse(int x)
    {
        int original = x;
        long long newX = abs((long long)x);
        long long result = 0;
        while (newX)
        {
            result = result * 10;
            result = result + (newX % 10);
            newX = newX / 10;
        }
        if (result > INT32_MAX)
        {
            return 0;
        }
        if (original < 0)
        {
            result = result * -1;
        }
        return result;
    }
};
;
