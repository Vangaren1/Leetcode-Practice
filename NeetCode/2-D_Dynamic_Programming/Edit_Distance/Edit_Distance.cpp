// Edit_Distance.cpp
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
    int minDistance(string word1, string word2)
    {
        return cost(word1, word2, word1.size(), word2.size());
    }

    int cost(const string &w1, const string &w2, int m, int n)
    {
        if (m == 0)
        {
            return n;
        }

        if (n == 0)
        {
            return m;
        }

        if (w1[m - 1] == w2[n - 1])
        {
            return cost(w1, w2, m - 1, n - 1);
        }

        int subCost = 1 + cost(w1, w2, m - 1, n - 1);
        int delCost = 1 + cost(w1, w2, m - 1, n);
        int insCost = 1 + cost(w1, w2, m, n - 1);
        return min(subCost, delCost, insCost);
    }
};

/*

This recursive solution will work, but is O(3^(m+n)).  Way too slow for leetcode.  Basically a brute force solution
class Solution
{
public:
    int minDistance(string word1, string word2)
    {
        return cost(word1, word2, word1.size(), word2.size());
    }

    int cost(const string &w1, const string &w2, int m, int n)
    {
        if( m == 0){
            return n;
        }

        if( n == 0){
            return m;
        }

        if( w1[m-1] == w2[n-1]){
            return cost(w1, w2, m-1, n-1);
        }

        int subCost = 1 + cost(w1, w2, m-1, n-1);
        int delCost = 1 + cost(w1, w2, m-1, n);
        int insCost = 1+ cost(w1, w2, m, n-1);
        return min(subCost, delCost, insCost);
    }
};
*/