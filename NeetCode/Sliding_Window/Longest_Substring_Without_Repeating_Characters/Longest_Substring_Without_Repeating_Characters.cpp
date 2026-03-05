// Longest_Substring_Without_Repeating_Characters.cpp
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
    int lengthOfLongestSubstring(string s)
    {
        vector<int> seen(128, 0);
        int longest{0}, left{0}, right{0};

        while (right < s.size() && left < s.size())
        {
            seen[s[right]]++;
            while (seen[s[right]] > 1)
            {
                seen[s[left]]--;
                left++;
            }
            longest = max(longest, right - left + 1);
            right++;
        }

        return longest;
    }
};
