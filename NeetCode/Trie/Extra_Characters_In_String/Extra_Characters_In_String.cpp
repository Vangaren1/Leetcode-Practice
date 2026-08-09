// Extra_Characters_In_String.cpp
//
// Compile locally with:
// clang++ Extra_Characters_In_String.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
private:
    struct TrieNode
    {
        bool terminal = false;
        unordered_map<char, TrieNode *> children;
    };

    TrieNode *root = new TrieNode();

    void insert(const string &s)
    {
        TrieNode *ptr = root;
        for (char ch : s)
        {
            if (ptr->children.count(ch) == 0)
            {
                ptr->children[ch] = new TrieNode();
            }
            ptr = ptr->children[ch];
        }
        ptr->terminal = true;
    }

public:
    int minExtraChar(string s, vector<string> &dictionary)
    {
        for (auto &word : dictionary)
        {
            insert(word);
        }

        int n = s.size();
        vector<int> dp(n + 1, 0);
        for (int index = n - 1; index >= 0; index--)
        {
            dp[index] = 1 + dp[index + 1];
            TrieNode *ptr = root;
            for (int j = index; j < n; j++)
            {
                if (ptr->children.count(s[j]) == 0)
                {
                    break;
                }
                ptr = ptr->children[s[j]];
                if (ptr->terminal)
                {
                    dp[index] = min(dp[index], dp[j + 1]);
                }
            }
        }
        return dp[0];
    }
};

int main()
{
    cout << "Running Extra_Characters_In_String.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
