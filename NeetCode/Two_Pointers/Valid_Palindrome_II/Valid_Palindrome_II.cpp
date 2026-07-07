// Valid_Palindrome_II.cpp
//
// Compile locally with:
// clang++ Valid_Palindrome_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool validPalindrome(string s)
    {
        int left(0);
        int right = s.size() - 1;
        while (left < right)
        {
            if (s[left] != s[right])
            {
                return palinSkip(s, left) || palinSkip(s, right);
            }
            left++;
            right--;
        }
        return true;
    }
    bool palinSkip(string s, int n)
    {
        int left(0);
        int right = s.size() - 1;
        while (left < right)
        {
            if (left == n)
            {
                left++;
            }
            else if (right == n)
            {
                right--;
            }
            if (s[left] != s[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};

int main()
{
    cout << "Running Valid_Palindrome_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
