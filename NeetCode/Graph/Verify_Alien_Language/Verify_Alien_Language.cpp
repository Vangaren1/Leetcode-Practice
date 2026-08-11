// Verify_Alien_Language.cpp
//
// Compile locally with:
// clang++ Verify_Alien_Language.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool isAlienSorted(vector<string> &words, string order)
    {
        unordered_map<char, int> alien;
        for (int index = 0; index < order.size(); index++)
        {
            alien[order[index]] = index;
        }

        int ptr = 0;
        bool match = true;

        for (int w = 0; w < words.size() - 1; w++)
        {
            string word1 = words[w];
            string word2 = words[w + 1];

            ptr = 0;
            match = true;

            while (ptr < word1.size() && ptr < word2.size() && match)
            {
                if (alien[word1[ptr]] > alien[word2[ptr]])
                {
                    return false;
                }
                else if (alien[word1[ptr]] < alien[word2[ptr]])
                {
                    match = false;
                }

                ptr++;
            }
            if (match && word2.size() < word1.size())
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    cout << "Running Verify_Alien_Language.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
