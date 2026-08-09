// Reorganize_String.cpp
//
// Compile locally with:
// clang++ Reorganize_String.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    string reorganizeString(string s)
    {
        unordered_map<char, int> count;
        int maxCount = -1;
        for (auto &ch : s)
        {
            count[ch]++;
            maxCount = max(maxCount, count[ch]);
        }

        if (maxCount > (s.size() + 1) / 2)
        {
            return "";
        }

        priority_queue<pair<int, char>> pq;
        for (const auto &[key, value] : count)
        {
            pq.push({value, key});
        }

        string result = "";
        pair<int, char> prev = {-1, 'n'};

        while (!pq.empty())
        {
            pair<int, char> tmp = pq.top();
            pq.pop();

            result = result + tmp.second;
            tmp.first--;

            if (prev.first != -1)
            {
                pq.push(prev);
            }

            if (tmp.first > 0)
            {
                prev = tmp;
            }
            else
            {
                prev = {-1, 'n'};
            }
        }
        return result;
    }
};

int main()
{
    cout << "Running Reorganize_String.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
