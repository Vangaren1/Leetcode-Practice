// Roman_To_Integer.cpp
//
// Compile locally with:
// clang++ Roman_To_Integer.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int romanToInt(string s)
    {
        unordered_map<char, int> roman = {{'I', 1},
                                          {'V', 5},
                                          {'X', 10},
                                          {'L', 50},
                                          {'C', 100},
                                          {'D', 500},
                                          {'M', 1000}};

        int total = 0;

        for (int index = 0; index < s.size() - 1; index++)
        {
            if (index < s.size() - 2 && roman[s[index]] < roman[s[index + 1]])
            {
                total -= roman[s[index]];
            }
            else
            {
                total += roman[s[index]];
            }
        }
        return total;
    }
}
}
;

int main()
{
    cout << "Running Roman_To_Integer.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
