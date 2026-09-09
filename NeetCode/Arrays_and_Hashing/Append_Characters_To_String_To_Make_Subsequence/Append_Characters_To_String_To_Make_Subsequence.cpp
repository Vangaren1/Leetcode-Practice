// Append_Characters_To_String_To_Make_Subsequence.cpp
//
// Compile locally with:
// clang++ Append_Characters_To_String_To_Make_Subsequence.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int appendCharacters(string s, string t)
    {
        int tPtr = 0;

        for (auto &ch : s)
        {
            if (tPtr < t.size() && ch == t[tPtr])
            {
                tPtr++;
            }
        }
        return t.size() - tPtr;
    }
};

int main()
{
    cout << "Running Append_Characters_To_String_To_Make_Subsequence.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
