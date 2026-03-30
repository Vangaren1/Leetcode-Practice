// check_if_strings_can_be_made_equal_I.cpp
//
// Compile locally with:
// clang++ check_if_strings_can_be_made_equal_I.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool canBeEqual(string s1, string s2)
    {
        array<int, 26> even1;
        array<int, 26> odd1;
        array<int, 26> even2;
        array<int, 26> odd2;

        for (int idx = 0; idx < s1.size(); idx++)
        {
            if (idx % 2 == 0)
            {
                even1[s1[idx] - 'a']++;
                even2[s2[idx] - 'a']++;
            }
            else
            {
                odd1[s1[idx] - 'a']++;
                odd2[s2[idx] - 'a']++;
            }
        }
        return even1 == even2 && odd1 == odd2;
    }
};

int main()
{
    cout << "Running check_if_strings_can_be_made_equal_I.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
