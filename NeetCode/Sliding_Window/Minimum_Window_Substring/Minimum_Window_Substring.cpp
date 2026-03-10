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
    bool checkInclusion(string s1, string s2)
    {
        if (s2.size() < s1.size())
        {
            return false;
        }
        vector<int> count(26, 0), window(26, 0);

        int right{0};

        while (right < s1.size())
        {
            window[s2[right] - 'a']++;
            count[s1[right] - 'a']++;
            right++;
        }

        while (right < s2.size())
        {
            if (count == window)
            {
                return true;
            }

            window[s2[right] - 'a']++;
            window[s2[right - s1.size()] - 'a']--;
            right++;
        }
        return count == window;
    }
};
