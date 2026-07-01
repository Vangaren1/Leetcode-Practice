// Majority_Element.cpp
//
// Compile locally with:
// clang++ Majority_Element.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int majorityElement(vector<int> &nums)
    {
        unordered_map<int, int> count;
        for (auto &num : nums)
        {
            count[num]++;
            if (count[num] > nums.size() / 2)
            {
                return num;
            }
        }
        return nums[0];
    }
};

int main()
{
    cout << "Running Majority_Element.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
