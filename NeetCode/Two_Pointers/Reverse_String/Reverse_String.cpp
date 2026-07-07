// Reverse_String.cpp
//
// Compile locally with:
// clang++ Reverse_String.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    void reverseString(vector<char> &s)
    {
        char tmp;
        int n = s.size();
        for (int index = 0; index < n / 2; index++)
        {
            tmp = s[index];
            s[index] = s[n - 1 - index];
            s[n - 1 - index] = tmp;
        }
    }
};

int main()
{
    cout << "Running Reverse_String.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
