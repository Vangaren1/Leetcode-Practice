// Merge_Strings_Alternately.cpp
//
// Compile locally with:
// clang++ Merge_Strings_Alternately.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    string mergeAlternately(string word1, string word2)
    {
        int ptr1(0), ptr2(0);
        string result;
        while (ptr1 < word1.size() && ptr2 < word2.size())
        {
            result += word1[ptr1];
            result += word2[ptr2];
            ptr1++;
            ptr2++;
        }
        if (ptr1 < word1.size())
        {
            return result + word1.substr(ptr1, word2.size());
        }
        return result + word2.substr(ptr2, word2.size());
    }
};

int main()
{
    cout << "Running Merge_Strings_Alternately.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
