// Minimum_Window_Substring.cpp
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
    string minWindow(string s, string t)
    {
        if (s.size() < t.size())
        {
            return "";
        }

        vector<int> chCnt(128, 0);
        vector<int> tCnt(128, 0);
        int left{0}, right{0};

        for (char ch : t)
        {
            tCnt[ch]++;
        }

        int minStart{0}, minLen{INT_MAX};

        while (left < s.size())
        {
            while (right < s.size() && !contains(chCnt, tCnt))
            {
                chCnt[s[right]]++;
                right++;
            }
            if (contains(chCnt, tCnt) && minLen > (right - left))
            {
                minStart = left;
                minLen = right - left;
            }

            chCnt[s[left]]--;
            left++;
        }
        return minLen == INT_MAX ? "" : s.substr(minStart, minLen);
    }

    bool contains(vector<int> &A, vector<int> &B)
    {

        for (int index = 0; index < A.size(); index++)
        {
            if (A[index] < B[index])
            {
                return false;
            }
        }
        return true;
    }
};
