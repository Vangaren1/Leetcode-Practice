// Longest_Common_Subsequence.cpp
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
private:
    struct PairHash
    {
        size_t operator()(const pair<string, string> &p) const
        {
            size_t h1 = hash<string>{}(p.first);
            size_t h2 = hash<string>{}(p.second);
            return h1 ^ (h2 << 1);
        }
    };
    unordered_map<pair<string, string>, int, PairHash> seen;

public:
    int longestCommonSubsequence(string text1, string text2)
    {
        seen[{"", ""}] = 0;

        return rec(text1, text2, 0, 0);
    }
    int rec(string &a, string &b, int ptr1, int ptr2)
    {

        if (seen.count({a.substr(ptr1), b.substr(ptr2)}))
        {
            return seen[{a.substr(ptr1), b.substr(ptr2)}];
        }
        if (a.substr(ptr1).size() == 0 || b.substr(ptr2).size() == 0)
        {
            return 0;
        }

        if (a[ptr1] == b[ptr2])
        {
            seen[{a.substr(ptr1), b.substr(ptr2)}] = 1 + rec(a, b, ptr1 + 1, ptr2 + 1);
            return seen[{a.substr(ptr1), b.substr(ptr2)}];
        }
        int first = rec(a, b, ptr1 + 1, ptr2);
        int second = rec(a, b, ptr1, ptr2 + 1);
        seen[{a.substr(ptr1), b.substr(ptr2)}] = max(first, second);
        return seen[{a.substr(ptr1), b.substr(ptr2)}];
    }
};
