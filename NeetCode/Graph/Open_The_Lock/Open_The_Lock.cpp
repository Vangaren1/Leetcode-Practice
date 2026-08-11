// Open_The_Lock.cpp
//
// Compile locally with:
// clang++ Open_The_Lock.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int openLock(vector<string> &deadends, string target)
    {
        unordered_map<char, pair<char, char>> upDown = {
            {'0', {'9', '1'}},
            {'1', {'0', '2'}},
            {'2', {'1', '3'}},
            {'3', {'2', '4'}},
            {'4', {'3', '5'}},
            {'5', {'4', '6'}},
            {'6', {'5', '7'}},
            {'7', {'6', '8'}},
            {'8', {'7', '9'}},
            {'9', {'8', '0'}}};
        unordered_set<string> visited;
        unordered_set<string> dead;
        for (auto &d : deadends)
        {
            dead.insert(d);
        }
        if (dead.count("0000"))
        {
            return -1;
        }
        if (target == "0000")
        {
            return 0;
        }
        queue<pair<string, int>> que;
        que.push({"0000", 0});
        visited.insert("0000");

        while (!que.empty())
        {
            auto [node, dist] = que.front();
            que.pop();

            for (int i = 0; i < 4; i++)
            {
                char original = node[i];
                auto [down, up] = upDown[original];
                for (char dir : {down, up})
                {
                    node[i] = dir;
                    if (!dead.count(node))
                    {
                        if (node == target)
                        {
                            return dist + 1;
                        }
                        if (!visited.count(node))
                        {
                            visited.insert(node);
                            que.push({node, dist + 1});
                        }
                    }
                }
                node[i] = original;
            }
        }

        return -1;
    }
};

int main()
{
    cout << "Running Open_The_Lock.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
