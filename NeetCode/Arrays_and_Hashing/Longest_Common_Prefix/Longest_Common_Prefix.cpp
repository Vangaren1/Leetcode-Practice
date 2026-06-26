// Longest_Common_Prefix.cpp
//
// Compile locally with:
// clang++ Longest_Common_Prefix.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
//
// NOTE:
// - Remove main() before submitting to LeetCode.
// - Keep only the class Solution definition.
//

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
    string longestCommonPrefix(vector<string> &strs)
    {
        for (int index = 0; index < strs[0].size(); index++)
        {
            for (auto &s : strs)
            {
                if (s.size() - 1 < index || s[index] != strs[0][index])
                {
                    return s.substr(0, index);
                }
            }
        }
        return strs[0];
    }
};

int main()
{
    cout << "Running Longest_Common_Prefix.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
