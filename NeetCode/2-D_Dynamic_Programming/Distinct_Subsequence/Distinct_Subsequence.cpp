// Distinct_Subsequence.cpp
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
    int numDistinct(string s, string t)
    {
        vector<vector<int>> cache(s.size(), vector<int>(t.size(), -1));
        return recursive(s, t, 0, 0, cache);
    }
    int recursive(string &s,
                  string &t,
                  int indexS,
                  int indexT,
                  vector<vector<int>> &cache)
    {
        if (indexT == t.size())
        {
            return 1;
        }
        if (indexS == s.size())
        {
            return 0;
        }
        if (cache[indexS][indexT] != -1)
        {
            return cache[indexS][indexT];
        }

        int total = 0;
        if (s[indexS] == t[indexT])
        {
            total += recursive(s, t, indexS + 1, indexT + 1, cache);
        }
        total += recursive(s, t, indexS + 1, indexT, cache);
        return cache[indexS][indexT] = total;
    }
};
