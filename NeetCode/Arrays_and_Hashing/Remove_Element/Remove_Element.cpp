// Remove_Element.cpp
//
// Compile locally with:
// clang++ Remove_Element.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int removeElement(vector<int> &nums, int val)
    {
        unordered_map<int, int> count;
        for (auto &num : nums)
        {
            count[num]++;
        }
        int k = (int)nums.size() - count[val];
        int ptr = 0;
        count[val] = 0;
        for (auto &[key, value] : count)
        {

            for (int i = 0; i < value; i++)
            {
                nums[ptr + i] = key;
            }
            ptr = ptr + value;
        }
        return k;
    }
};

int main()
{
    cout << "Running Remove_Element.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
