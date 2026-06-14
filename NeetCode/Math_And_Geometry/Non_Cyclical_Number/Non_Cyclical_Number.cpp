// Non_Cyclical_Number.cpp
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
    bool isHappy(int n)
    {
        unordered_set<int> seen;
        while (n != 1)
        {
            if (seen.count(n))
            {
                return false;
            }
            seen.insert(n);
            n = sqSum(n);
        }
        return true;
    }
    int sqSum(int n)
    {
        int total = 0;
        while (n)
        {
            total = total + (n % 10) * (n % 10);
            n = n / 10;
        }
        return total;
    }
};
