// Two_Sum.cpp
//
// Compile locally with:
// clang++ Two_Sum.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> pos;
        int tmp = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            tmp = nums[i];
            pos[target - tmp] = i;
        }

        for (int j = 0; j < nums.size(); j++)
        {
            tmp = nums[j];
            if (pos.find(tmp) != pos.end() && pos[tmp] != j)
            {
                return {j, pos[tmp]};
            }
        }
        return {};
    }
};

int main()
{
    cout << "Running Two_Sum.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
