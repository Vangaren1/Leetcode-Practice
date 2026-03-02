// Valid_Palindrome.cpp
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
    bool isPalindrome(string s)
    {

        string tmp;
        for (char ch : s)
        {
            if (isalnum(ch))
            {
                tmp += tolower(ch);
            }
        }
        int start = 0;
        int end = tmp.size() - 1;
        while (start <= end)
        {
            if (tmp[start] != tmp[end])
            {
                return false;
            }

            start++;
            end--;
        }
        return true;
    }
};
