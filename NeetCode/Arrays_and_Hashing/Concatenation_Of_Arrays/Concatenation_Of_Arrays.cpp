// Concatenation_Of_Arrays.cpp
//
// Compile locally with:
// clang++ Concatenation_Of_Arrays.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> getConcatenation(vector<int> &nums)
    {
        nums.insert(nums.end(), nums.begin(), nums.end());
        return nums;
    }
};

int main()
{
    cout << "Running Concatenation_Of_Arrays.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
