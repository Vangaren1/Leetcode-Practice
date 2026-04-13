// Palindrome_Partition.cpp
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
    vector<vector<string>> partition(string s)
    {
        vector<vector<string>> results;
        vector<string> curr;
        dfs(s, 0, results, curr);
        return results;
    }

    void dfs(string &s, int index, vector<vector<string>> &results, vector<string> &curr)
    {
        if (index >= s.size())
        {
            results.push_back(curr);
            return;
        }

        for (int idx = index; idx < s.size(); idx++)
        {
            string sub = s.substr(index, idx - index + 1);
            if (isPalindrome(sub))
            {
                curr.push_back(sub);
                dfs(s, idx + 1, results, curr);
                curr.pop_back();
            }
        }
    }
    bool isPalindrome(string s)
    {
        int start = 0;
        int end = s.size() - 1;
        while (start < end)
        {
            if (s[start] != s[end])
            {
                return false;
            }

            start++;
            end--;
        }
        return true;
    }
};
