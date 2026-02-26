// Sort_Integers_By_Number_of_1_Bits.cpp
//
// Compile locally with:
// clang++ Sort_Integers_By_Number_of_1_Bits.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> sortByBits(vector<int> &arr)
    {
        vector<pair<int, int>> bitCount;
        for (int num : arr)
        {
            pair<int, int> tmp = {__builtin_popcount(num), num};
            bitCount.push_back(tmp);
        }
        sort(bitCount.begin(), bitCount.end());
        vector<int> results;
        for (pair n : bitCount)
        {
            results.push_back(n.second);
        }
        return results;
    }
};

int main()
{
    cout << "Running Sort_Integers_By_Number_of_1_Bits.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
