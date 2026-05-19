// Hand_Of_Straights.cpp
//
// Compile locally with:
// clang++ Hand_Of_Straights.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool isNStraightHand(vector<int> &hand, int groupSize)
    {
        int n = hand.size();
        if (n % groupSize != 0)
        {
            return false;
        }

        unordered_map<int, int> count;

        for (int card : hand)
        {
            count[card]++;
        }

        vector<int> keys;

        for (const auto &[card, count] : count)
        {
            keys.push_back(card);
        }
        sort(keys.begin(), keys.end());

        for (int cardVal : keys)
        {
            while (count[cardVal] > 0)
            {
                for (int x = cardVal; x < cardVal + groupSize; x++)
                {
                    if (count[x] == 0)
                    {
                        return false;
                    }
                    count[x]--;
                }
            }
        }
        return true;
    };

    int main()
    {
        cout << "Running Hand_Of_Straights.cpp..." << endl;

        Solution sol;

        // TODO:
        // Add local test calls here

        return 0;
    }
