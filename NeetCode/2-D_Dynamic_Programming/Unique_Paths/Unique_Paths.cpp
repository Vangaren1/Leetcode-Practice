// Unique_Paths.cpp
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
    int uniquePaths(int m, int n)
    {
        int a = m - 1;
        int b = n - 1;
        return (int)comb(a + b, b);
    }
    long long comb(int a, int b)
    {
        if (b < 0 or b > a)
        {
            return 0;
        }
        if (b == 0 || b == a)
        {
            return 1;
        }
        b = min(b, a - b);
        long long result = 1;
        for (int i = 1; i <= b; i++)
        {
            result = result * (a - b + i) / i;
        }
        return result;
    }
};
