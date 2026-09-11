// Count_Vowel_String_In_Ranges.cpp
//
// Compile locally with:
// clang++ Count_Vowel_String_In_Ranges.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> vowelStrings(vector<string> &words, vector<vector<int>> &queries)
    {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        vector<int> dp = {0};

        for (auto &word : words)
        {
            int valid = 0;
            if (vowels.count(word[0]) > 0 && vowels.count(word[word.size() - 1]) > 0)
            {
                valid = 1;
            }
            dp.push_back(dp.back() + valid);
        }

        vector<int> results;

        for (auto &tmp : queries)
        {
            int left = tmp[0];
            int right = tmp[1];

            results.push_back(dp[right + 1] - dp[left]);
        }
        return results;
    }
};

int main()
{
    cout << "Running Count_Vowel_String_In_Ranges.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
