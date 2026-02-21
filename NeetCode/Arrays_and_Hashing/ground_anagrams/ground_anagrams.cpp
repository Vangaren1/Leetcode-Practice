// ground_anagrams.cpp
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
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> dict;
        for (string st : strs)
        {
            string tmp = st;
            sort(tmp.begin(), tmp.end());
            dict[tmp].push_back(st);
        }

        vector<vector<string>> result;

        for (const auto &[key, value] : dict)
        {
            result.push_back(value);
        }
        return result;
    }
};
