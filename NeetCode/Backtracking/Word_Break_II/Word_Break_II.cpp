// Word_Break_II.cpp
//
// Compile locally with:
// clang++ Word_Break_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    unordered_set<string> words;
    int n;
    vector<string> curr;
    vector<string> results;

public:
    vector<string> wordBreak(string s, vector<string> &wordDict)
    {
        n = s.size();
        for (auto &word : wordDict)
        {
            words.insert(word);
        }

        backtrack(0, s);

        return results;
    }

    void backtrack(int index, string s)
    {
        if (index == n)
        {
            string sentence;

            for (int i = 0; i < curr.size(); i++)
            {
                if (i > 0)
                {
                    sentence += " ";
                }

                sentence += curr[i];
            }
            results.push_back(sentence);
        }

        for (auto &word : words)
        {
            string tmp(s.substr(index, word.size()));
            if (word != tmp)
            {
                continue;
            }

            curr.push_back(word);
            backtrack(index + word.size(), s);
            curr.pop_back();
        }
    }
};

int main()
{
    cout << "Running Word_Break_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
