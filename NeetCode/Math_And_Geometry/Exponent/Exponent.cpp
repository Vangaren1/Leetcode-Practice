// Exponent.cpp
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
    double myPow(double x, int n)
    {
        if (x == 0)
        {
            return 0;
        }
        if (n == 0)
        {
            return 1;
        }
        if (n == 1)
        {
            return x;
        }

        if (n < 0)
        {
            return 1.0 / myPow(x, abs(n));
        }

        if (n % 2 == 0)
        {
            double result = myPow(x, n / 2);
            return result * result;
        }

        return myPow(x, n - 1) * x;
    }
};
