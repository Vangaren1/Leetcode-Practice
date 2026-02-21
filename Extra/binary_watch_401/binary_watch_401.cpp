// binary_watch_401.cpp
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
#include <format>

using namespace std;

class Solution
{
public:
    vector<string> readBinaryWatch(int turnedOn)
    {
        int hour, minute;
        vector<string> retVal;
        std::string result;
        for (int n = 0; n < 1 << 10; n++)
        {

            if (__builtin_popcount((unsigned)n) != turnedOn)
                continue;

            hour = 0xF & (n >> 6);
            minute = 0x3F & n;
            if (hour < 12 && minute < 60)
            {
                result = to_string(hour) + ":" + (minute < 10 ? "0" : "") + to_string(minute);
                retVal.push_back(result);
            }
        }
        return retVal;
    }
};
